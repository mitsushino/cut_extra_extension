# -*- coding: utf-8 -*-

import configparser
import os
import shutil
import unittest
from send2trash import send2trash
from cut_extra_extension import cut_extra_extension
from cut_extra_extension import get_designated_path
from cut_extra_extension import move_file_to_designated_path


class CutExtensionTest(unittest.TestCase):
    '''テスト用URLと正解URLをテキストから読み込み
       各URLを比較してcut_extra_extensionが正常に動作しているか
       確認するユニットテスト
    '''

    # テスト用URL読み込み
    cut_urls = []
    with open('test_urls.txt', encoding='utf-8') as f:
        for line in f:
            cut_urls.append(line.rstrip())

    # 正解用URL読み込み
    correct_urls = []
    with open('correct_urls.txt', encoding='utf-8') as f:
        for line in f:
            correct_urls.append(line.rstrip())

    def test_cut_extra_extension(self):
        while self.cut_urls:
            self.assertEqual(cut_extra_extension(self.cut_urls.pop(0)),
                             self.correct_urls.pop(0))


class FileMoveTest(unittest.TestCase):
    def test_get_designated_path(self):
        '''iniファイルを読み取り、ファイルの移動先パスを取得するテスト'''
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        designated_path = config['PASS']['copy_path']
        self.assertEqual(get_designated_path(), designated_path)

    def test_copy_file(self):
        '''
        ファイルを移動するテスト
        '''
        # テスト用の移動先フォルダ作成
        folder_path = os.path.join(os.getcwd(), 'copy_dist')
        if os.path.exists(folder_path):
            send2trash(folder_path)
        os.mkdir(folder_path)

        # テスト用ファイル作成
        test_file = 'mp4.mp4'
        exception_test_file = 'mp42.mp4'
        exe_file = 'test.exe'
        ini_file = 'test.ini'
        with open(test_file, mode='w', encoding='utf-8') as f: pass
        with open(exception_test_file, mode='w', encoding='utf-8') as f: pass
        shutil.move(exception_test_file, folder_path)
        with open(exception_test_file, mode='w', encoding='utf-8') as f: pass
        with open(exe_file, mode='w', encoding='utf-8') as f: pass
        with open(ini_file, mode='w', encoding='utf-8') as f: pass

        # テスト実行
        self.assertEqual(os.path.join(os.getcwd(), 'copy_dist', test_file),
                         move_file_to_designated_path(folder_path, test_file))
        self.assertRaises(OSError,
                          move_file_to_designated_path(folder_path, exception_test_file))
        self.assertEqual(None,
                         move_file_to_designated_path(folder_path, exe_file))
        self.assertEqual(None,
                         move_file_to_designated_path(folder_path, ini_file))


if __name__ == '__main__':
    unittest.main()
