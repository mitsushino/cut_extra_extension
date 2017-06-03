# -*- coding: utf-8 -*-
# ファイル名取得、変更処理参照元
# http://qiita.com/supersaiakujin/items/12451cd2b8315fe7d054

import configparser
import os
import shutil
import sys


def cut_extra_extension(file_name):
    '''
    拡張子以降の余分な文字列を削除し、正規化したファイル名にリネームする
    mp4.mp4mp4 -> mp4.mp4  mp4.mp4test.txt -> mp4.mp4  abcdef -> abcdef
    :param file_name:
    :return: 拡張子以降の余分な文字列を削除したファイル名
    '''
    try:
        while True:
            period_position = file_name.rindex('.')
            file_name = file_name[:period_position + 4]
            ext = file_name[-3:]
            if ext == 'mp4' or ext == 'vlc' or ext == 'exe' or ext == 'ini':
                print('{}を変換しています・・・'.format(file_name))
                return file_name
            else:
                file_name = file_name[:-4]
    except ValueError:
        print('ファイル名にドット(.)が存在しないため、次の変換を行います')
        return file_name


def get_designated_path():
    '''
    iniファイルを読み取り、ファイルのコピー先パスを取得する
    :return: ファイルのコピー先パス
    '''
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    return config['PASS']['copy_path']


def move_file_to_designated_path(path, f):
    '''
    ファイルを指定されたパスに移動する
    既にファイルが存在する場合は例外を出力して移動しない
    exeファイルは移動しない
    iniファイルは移動しない
    '''
    _, ext = os.path.splitext(f)
    if ext == '.exe' or ext == '.ini':
        return
    move_path = os.path.join(path, f)
    try:
        if os.path.exists(move_path):
            raise OSError
        print('{}を{}へ移動します'.format(f, path))
        return shutil.move(os.path.join(os.getcwd(), f),
                           move_path)

    except OSError:
        print('{}が移動先フォルダ既に存在します。コピーしません。'.format(f))


if __name__ == '__main__':
    # 余分な拡張子の削除処理
    answer = input('ファイルの拡張子の余計な部分を削除しますか？[y/n]')
    if answer != 'y':
        sys.exit(0)
    current_folder_files = os.listdir('.')
    for f in current_folder_files:
        print('{}を変換します'.format(f))
        os.rename(f, cut_extra_extension(f))

    # ファイルのコピー処理
    current_folder_files = os.listdir('.')
    designated_path = get_designated_path()
    for f in current_folder_files:
        move_file_to_designated_path(designated_path, f)

    input('処理が完了しました')
