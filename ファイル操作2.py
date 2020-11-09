"""
TV(h.265)内にあるアニメフォルダーを放送年に合わせて移動するプログラムである。
"""

import shutil
import os
import glob
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
e_2006 = s_2006+4

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

s_2015 = e_2014+1
e_2015 = s_2015+13

s_2016 = e_2015+1
e_2016 = s_2016+8

s_2017 = e_2016+1
e_2017 = s_2017+10

s_2018 = e_2017+1
e_2018 = s_2018+32

path = "C:\\prog\\git\\rename\\フォルダ一覧(py).txt"
path1 = "D:\\TV(h.265)"


def foldercpy(start, end, year):
    for num in range(start, end):  # path生成

        title = os.path.join(path1, l[num])

        if (os.path.exists(title) == True):  # ファイル・フォルダの存在確

            title2 = os.path.join(path1, os.path.join(year, l[num]))

            print(title+"をコピーします")
            new_path = dir_util.copy_tree(title, title2)  # フォルダコピー
            print(new_path)

            shutil.rmtree(title)  # 元のフォルダ削除


with open(path,"r",encoding="utf-8") as f:
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

    foldercpy(s_2010, e_2010, "2010")

    foldercpy(s_2011, e_2011, "2011")

    foldercpy(s_2012, e_2012, "2012")

    foldercpy(s_2013, e_2013, "2013")

    foldercpy(s_2014, e_2014, "2014")

    foldercpy(s_2015, e_2015, "2015")

    foldercpy(s_2016, e_2016, "2016")

    foldercpy(s_2017, e_2017, "2017")

    foldercpy(s_2018, e_2018, "2018")
    
with open(r"C:\prog\git\rename\2019.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 100, "2019")
    except:
        pass

with open(r"C:\prog\git\rename\2019.txt", encoding="utf-8") as f:
    l = [s.strip() for s in f.readlines()]
    try:
        foldercpy(0, 150, "2020")
    except:
        pass
