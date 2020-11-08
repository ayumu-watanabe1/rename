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
e_2006 = s_2006+3

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
e_2014 = s_2014+17

s_2015 = e_2014+1
e_2015 = s_2015+13

s_2016 = e_2015+1
e_2016 = s_2016+8

s_2017 = e_2016+1
e_2017 = s_2017+10

s_2018 = e_2017+1
e_2018 = s_2018+32

s_2019 = e_2018+1
e_2019 = s_2019+57

s_2020 = e_2019+1
e_2020 = s_2020+109

path = "D:\\TV(h.265)\\フォルダ一覧(py).txt"
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

        os.chdir(os.path.join(path1, os.path.join(year, l[num])))
        Rename()


path2 = r"D:\TV(h.265)\映画"
path3 = r"D:\TV(h.265)\夏目友人帳シリーズ\夏目友人帳"
path4 = r"D:\TV(h.265)\夏目友人帳シリーズ\夏目友人帳 陸"
path5 = r"D:\TV(h.265)\夏目友人帳シリーズ\続 夏目友人帳"
path6 = r"D:\TV(h.265)\ANIMAX MUSIX"
os.chdir(path6)
Rename()

with open(path) as f:
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

    searchfolder(s_2010, e_2010, "2010")

    searchfolder(s_2011, e_2011, "2011")

    searchfolder(s_2012, e_2012, "2012")

    searchfolder(s_2013, e_2013, "2013")

    searchfolder(s_2014, e_2014, "2014")

    searchfolder(s_2015, e_2015, "2015")

    searchfolder(s_2016, e_2016, "2016")

    searchfolder(s_2017, e_2017, "2017")

    searchfolder(s_2018, e_2018, "2018")

    searchfolder(s_2019, e_2019, "2019")

    searchfolder(s_2020, e_2020, "2020")
