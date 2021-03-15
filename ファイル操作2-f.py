"""
TV(h.265)内にあるアニメフォルダーを放送年に合わせて移動するプログラムである。
"""

import shutil
import os
import glob
import subprocess
from distutils import dir_util


path1 = "E:\\TV"
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


with open(r"C:\prog\rename\1999.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 150, "1999")
    except:
        pass

with open(r"C:\prog\rename\2000.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2000")
    except:
        pass

with open(r"C:\prog\rename\2001.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2001")
    except:
        pass

with open(r"C:\prog\rename\2002.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2002")
    except:
        pass

with open(r"C:\prog\rename\2003.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2003")
    except:
        pass

with open(r"C:\prog\rename\2004.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2004")
    except:
        pass


with open(r"C:\prog\rename\2005.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2005")
    except:
        pass

with open(r"C:\prog\rename\2006.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2006")
    except:
        pass

with open(r"C:\prog\rename\2007.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2007")
    except:
        pass

with open(r"C:\prog\rename\2008.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2008")
    except:
        pass


with open(r"C:\prog\rename\2009.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2009")
    except:
        pass


with open(r"C:\prog\rename\2010.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2010")
    except:
        pass

with open(r"C:\prog\rename\2011.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2011")
    except:
        pass

with open(r"C:\prog\rename\2012.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2012")
    except:
        pass

with open(r"C:\prog\rename\2013.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2013")
    except:
        pass

with open(r"C:\prog\rename\2014.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2014")
    except:
        pass


with open(r"C:\prog\rename\2015.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2015")
    except:
        pass

with open(r"C:\prog\rename\2016.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2016")
    except:
        pass

with open(r"C:\prog\rename\2017.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2017")
    except:
        pass

with open(r"C:\prog\rename\2018.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2018")
    except:
        pass


with open(r"C:\prog\rename\2019.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2019")
    except:
        pass

with open(r"C:\prog\rename\2020.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 150, "2020")
    except:
        pass

with open(r"C:\prog\rename\2021.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 150, "2021")
    except:
        pass
