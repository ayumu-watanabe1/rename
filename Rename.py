"""
余計な文字列や文字を検出し削除するプログラムである。

"""


import string
import os
import glob
import re

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
e_2009 = s_2009+4

s_2010 = e_2009+1
e_2010 = s_2010+8

s_2011 = e_2010+1
e_2011 = s_2011+10

s_2012 = e_2011+1
e_2012 = s_2012+9

s_2013 = e_2012+1
e_2013 = s_2013+5

s_2014 = e_2013+1
e_2014 = s_2014+18

path = r"C:\prog\git\rename\フォルダ一覧(py).txt"
path1 = "D:\\TV(h.265)"

print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
ans = input()
if re.search("yes", ans) or re.search("y", ans):
    delete = "1"
else:
    delete = "0"


def RENAME_TRY(title, changetitle):
    try:
        os.rename(title, changetitle)
        print(title+"から"+changetitle+"へ変更しました。\n")
        title = changetitle
    except WindowsError:
        if delete == "1":
            os.remove(changetitle)
            print(changetitle+"は存在するため削除しました。\n")
            os.rename(title, changetitle)
            title = changetitle
        else:
            print("Error:"+title+"は既に存在するため処理がスキップされました。\n")


def Rename():
    for title in glob.glob("*.mp4"):

        if re.search("[0-9]{12}", title):

            changetitle = re.sub("^[0-9]{12}_", "", title)
            changetitle = re.sub("^[0-9]{12} ", "", changetitle)
            RENAME_TRY(title, changetitle)

        if re.search("＜アニメギルド＞", title):
            changetitle = re.sub("＜アニメギルド＞", "", title)
            changetitle = re.sub("アニメ", "", changetitle)
            RENAME_TRY(title, changetitle)
        
        if re.search("キッズステーション", title):
            changetitle = re.sub("キッズステーション", "KIDS", title)
            RENAME_TRY(title, changetitle)

        if re.search("TBSチャンネル", title):
            changetitle = re.sub("TBSチャンネル", "TBS", title)
            RENAME_TRY(title, changetitle)

        if re.search("日テレプラス", title):
            changetitle = re.sub("日テレプラス", "日テレ", title)
            RENAME_TRY(title, changetitle)

        if re.search("BSアニマックス", title):
            changetitle = re.sub("BSアニマックス", "BS", title)
            RENAME_TRY(title, changetitle)

        if re.search("TVアニメ", title):
            changetitle = re.sub("TVアニメ", "", title)

            RENAME_TRY(title, changetitle)

        if re.search("＜夜の集中放送＞", title):
            changetitle = re.sub("＜夜の集中放送＞", "", title)
            RENAME_TRY(title, changetitle)

        if re.search("【無料】", title):
            changetitle = re.sub("【無料】", "", title)
            RENAME_TRY(title, changetitle)

        if re.search("^「", title):
            changetitle = re.sub("^「", "", title)
            changetitle = re.sub("「", " ", changetitle)
            changetitle = re.sub("」", " ", changetitle)
            changetitle = re.sub("  ", " ", changetitle)
            changetitle = re.sub("   ", " ", changetitle)

            RENAME_TRY(title, changetitle)


def searchfolder(start, end, year):
    for num in range(start, end):  # path生成
        try:
            os.chdir(os.path.join(path1, os.path.join(year, l[num])))
            Rename()
        except WindowsError:
            pass


path2 = r"D:\TV(h.265)\映画"
path3 = r"D:\TV(h.265)\夏目友人帳シリーズ\夏目友人帳"
path4 = r"D:\TV(h.265)\夏目友人帳シリーズ\夏目友人帳 陸"
path5 = r"D:\TV(h.265)\夏目友人帳シリーズ\続 夏目友人帳"
path6 = r"D:\TV(h.265)\ANIMAX MUSIX"
#os.chdir(path6)
Rename()

with open(path, encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]

    searchfolder(s_1999, e_1999, "1999")

    searchfolder(s_2000, e_2000, "2000")

    searchfolder(s_2001, e_2001, "2001")

    searchfolder(s_2002, e_2002, "2002")

    searchfolder(s_2003, e_2003, "2003")

    searchfolder(s_2004, e_2004, "2004")

    searchfolder(s_2005, e_2005, "2005")

    searchfolder(s_2006, e_2006, "2006")

    searchfolder(s_2007, e_2007, "2007")

    searchfolder(s_2008, e_2008, "2008")

    searchfolder(s_2009, e_2009, "2009")

with open(r"C:\prog\git\rename\2010.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2010")
    except:
        pass

with open(r"C:\prog\git\rename\2011.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2011")
    except:
        pass

with open(r"C:\prog\git\rename\2012.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2012")
    except:
        pass

with open(r"C:\prog\git\rename\2013.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2013")
    except:
        pass

with open(r"C:\prog\git\rename\2014.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2014")
    except:
        pass

with open(r"C:\prog\git\rename\2015.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2015")
    except:
        pass

with open(r"C:\prog\git\rename\2016.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2016")
    except:
        pass

with open(r"C:\prog\git\rename\2017.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2017")
    except:
        pass

with open(r"C:\prog\git\rename\2018.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2018")
    except:
        pass

with open(r"C:\prog\git\rename\2019.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2019")
    except:
        pass
    
with open(r"C:\prog\git\rename\2020.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 200, "2020")
    except:
        pass
    
