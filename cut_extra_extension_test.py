# -*- coding: utf-8 -*-

import configparser
import unittest
from cut_extra_extension import cut_extra_extension
from cut_extra_extension import get_designated_path


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
    '''iniファイルを読み取り、ファイルのコピー先パスを取得するテスト'''
    def test_copy_file_to_designated_path(self):
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        designated_path = config['PASS']['copy_path']
        self.assertEqual(designated_path, get_designated_path())


if __name__ == '__main__':
    unittest.main()
