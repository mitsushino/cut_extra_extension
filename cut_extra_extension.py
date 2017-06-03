# -*- coding: utf-8 -*-
# ファイル名取得、変更処理参照元
# http://qiita.com/supersaiakujin/items/12451cd2b8315fe7d054

import sys
import os


def cut_extra_extension(file_name):
    try:
        while True:
            period_position = file_name.rindex('.')
            file_name = file_name[:period_position + 4]
            ext = file_name[-3:]
            if ext == 'mp4' or ext == 'vlc' or ext == 'exe':
                return file_name
            else:
                file_name = file_name[:-4]
    except ValueError:
        print('ファイル名にドット(.)が存在しないため、次の変換を行います')
        return file_name


if __name__ == '__main__':
    answer = input('ファイルの拡張子の余計な部分を削除しますか？[y/n]')
    if answer != 'y':
        sys.exit(0)
    current_folder_files = os.listdir('.')
    for f in current_folder_files:
        print('{}を変換しています・・・'.format(f))
        os.rename(f, cut_extra_extension(f))
    input('処理が完了しました')
