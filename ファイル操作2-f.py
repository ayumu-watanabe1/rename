"""
TV(h.265)内にあるアニメフォルダーを放送年に合わせて移動するプログラムである。
"""

import shutil
import os
import glob
import subprocess
from distutils import dir_util
import SyoboiCal


path1 = 'E:/TV'
#path1 = "D:\\TV_data"

def foldercpy(start, end, year):
    for num in range(start, end):  # path生成

        title = os.path.join(path1, l[num])

        if (os.path.exists(title) == True):  # ファイル・フォルダの存在確

            title2 = os.path.join(path1, os.path.join(year, l[num]))

            print(title+"をコピーします")
            if (os.path.isdir(title2) == False):  # ファイルが存在しない場合実行する
                try:
                    command2 = ["powershell", "-command", "New-Item",
                                "'"+title2+"'", "-Type", "Directory"]
                    subprocess.check_call(command2, shell=True)
                except:
                    pass
            try:
                command = ["powershell", "-Command", "Move-Item",
                           "'"+title+"\\*'", "'"+title2+"\\'"]
                command1 = ["powershell", "-Command", "rm",
                            "'"+title+"'"]
                subprocess.check_call(command, shell=True)
                subprocess.check_call(command1, shell=True)
            except:
                print("move-item error")
            # new_path = dir_util.copy_tree(title, title2)  # フォルダコピー
            # print(new_path)
            # shutil.rmtree(title)  # 元のフォルダ削除


#openPath = 'C:/prog/rename/dataset/'
startYear, endYear = 1999, 2021

for i in range(endYear - startYear + 1):
    l = []
    l = SyoboiCal.search_title(startYear+i, l)
    try:
        foldercpy(0, 150, str(startYear+i))
        #print(l)   #debug
    except:  # この書き方は公式でもあまり推奨されません..
        pass
