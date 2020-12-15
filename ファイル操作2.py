"""
TV(h.265)内にあるアニメフォルダーを放送年に合わせて移動するプログラムである。
"""

import shutil
import os
import glob
import subprocess
from distutils import dir_util

s_1999 = 1
e_1999 = s_1999+1

s_2000 = e_1999+1
e_2000 = s_2000+1

s_2001 = e_2000+1
e_2001 = s_2001+2

s_2002 = e_2001+1
e_2002 = s_2002+0

s_2003 = e_2002+1
e_2003 = s_2003+0

s_2004 = e_2003+1
e_2004 = s_2004+2

s_2005 = e_2004+1
e_2005 = s_2005+1

s_2006 = e_2005+1
e_2006 = s_2006+5

s_2007 = e_2006+1
e_2007 = s_2007+2

s_2008 = e_2007+1
e_2008 = s_2008+3

s_2009 = e_2008+1
e_2009 = s_2009+5

path = "C:\\prog\\git\\rename\\フォルダ一覧(py).txt"
path1 = "D:\\TV(h.265)"


def foldercpy(start, end, year):
    for num in range(start, end):  # path生成

        title = os.path.join(path1, l[num])

        if (os.path.exists(title) == True):  # ファイル・フォルダの存在確

            title2 = os.path.join(path1, os.path.join(year, l[num]))

            print(title+"をコピーします")
            if (os.path.isdir(title2) == False): #ファイルが存在しない場合実行する
                try:
                    command2 = ["powershell", "-command", "New-Item",
                                "'"+title2+"'","-Type","Directory"]
                    subprocess.check_call(command2,shell=True)
                except:
                    pass
            try:
                command = ["powershell","-Command","Move-Item","'"+title+"\\*'","'"+title2+"'"]
                command1 = ["powershell", "-Command", "rm",
                           "'"+title+"'"]
                subprocess.check_call(command, shell=True)
                subprocess.check_call(command1, shell=True)
            except:
                print("move-item error")
            #new_path = dir_util.copy_tree(title, title2)  # フォルダコピー
            #print(new_path)
            #shutil.rmtree(title)  # 元のフォルダ削除


with open(path, "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]

    foldercpy(s_1999, e_1999, "1999")

    foldercpy(s_2000, e_2000, "2000")

    foldercpy(s_2001, e_2001, "2001")

    foldercpy(s_2002, e_2002, "2002")

    foldercpy(s_2003, e_2003, "2003")

    foldercpy(s_2004, e_2004, "2004")

    foldercpy(s_2005, e_2005, "2005")

    foldercpy(s_2006, e_2006, "2006")

    foldercpy(s_2007, e_2007, "2007")

    foldercpy(s_2008, e_2008, "2008")

    foldercpy(s_2009, e_2009, "2009")

with open(r"C:\prog\git\rename\2010.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2010")
    except:
        pass

with open(r"C:\prog\git\rename\2011.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2011")
    except:
        pass

with open(r"C:\prog\git\rename\2012.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2012")
    except:
        pass

with open(r"C:\prog\git\rename\2013.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2013")
    except:
        pass

with open(r"C:\prog\git\rename\2014.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2014")
    except:
        pass


with open(r"C:\prog\git\rename\2015.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2015")
    except:
        pass

with open(r"C:\prog\git\rename\2016.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2016")
    except:
        pass

with open(r"C:\prog\git\rename\2017.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2017")
    except:
        pass

with open(r"C:\prog\git\rename\2018.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2018")
    except:
        pass


with open(r"C:\prog\git\rename\2019.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2019")
    except:
        pass

with open(r"C:\prog\git\rename\2020.txt", "r", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 150, "2020")
    except:
        pass
