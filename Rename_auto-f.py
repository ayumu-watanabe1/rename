"""
余計な文字列や文字を検出し削除するプログラムである。

"""


import string
import os
import glob
import re

path1 = "E:\\TV"
#path1=r"D:\TV_data"

#print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
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

        if re.search("キッズステーション", title):
            changetitle = re.sub("[キッズステーション]", "", title)
            RENAME_TRY(title, changetitle)

        if re.search("テレ朝チャンネル", title):
            changetitle = re.sub("テレ朝チャンネル", "テレ朝", title)
            RENAME_TRY(title, changetitle)

        if re.search("日テレプラス", title):
            changetitle = re.sub("日テレプラス", "日テレ", title)
            RENAME_TRY(title, changetitle)

        if re.search("TBSチャンネル", title):
            changetitle = re.sub("TBSチャンネル", "TBS", title)
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
# os.chdir(path6)
Rename()

with open(r"C:\prog\rename\1999.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "1999")
    except:
        pass

with open(r"C:\prog\rename\2000.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2000")
    except:
        pass
with open(r"C:\prog\rename\2001.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2001")
    except:
        pass
with open(r"C:\prog\rename\2002.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2002")
    except:
        pass
with open(r"C:\prog\rename\2003.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2003")
    except:
        pass
with open(r"C:\prog\rename\2004.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2004")
    except:
        pass
with open(r"C:\prog\rename\2005.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2005")
    except:
        pass
with open(r"C:\prog\rename\2006.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2006")
    except:
        pass
with open(r"C:\prog\rename\2007.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2007")
    except:
        pass
with open(r"C:\prog\rename\2008.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2008")
    except:
        pass
with open(r"C:\prog\rename\2009.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2009")
    except:
        pass


with open(r"C:\prog\rename\2010.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2010")
    except:
        pass

with open(r"C:\prog\rename\2011.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2011")
    except:
        pass

with open(r"C:\prog\rename\2012.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2012")
    except:
        pass

with open(r"C:\prog\rename\2013.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2013")
    except:
        pass

with open(r"C:\prog\rename\2014.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2014")
    except:
        pass

with open(r"C:\prog\rename\2015.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2015")
    except:
        pass

with open(r"C:\prog\rename\2016.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2016")
    except:
        pass

with open(r"C:\prog\rename\2017.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2017")
    except:
        pass

with open(r"C:\prog\rename\2018.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2018")
    except:
        pass

with open(r"C:\prog\rename\2019.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 100, "2019")
    except:
        pass

with open(r"C:\prog\rename\2020.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 200, "2020")
    except:
        pass


with open(r"C:\prog\rename\2021.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        searchfolder(0, 200, "2021")
    except:
        pass
