"""
余計な文字列や文字を検出し削除するプログラムである。

"""
import os
import glob
import re


def rename_try(title, changetitle,trigger):
    try:
        os.rename(title, changetitle)
        print(title+"から"+changetitle+"へ変更しました。\n")
        title = changetitle
    except WindowsError:
        if trigger == "1":
            os.remove(changetitle)
            print(changetitle+"は存在するため削除しました。\n")
            os.rename(title, changetitle)
            title = changetitle
        else:
            print("Error:"+title+"は既に存在するため処理がスキップされました。\n")


def rename(trigger):
    """ 関数rename_try に変更する名前を引数として渡す """
    for title in glob.glob("*.mp4"):

        if re.search("[0-9]{12}", title):

            changetitle = re.sub("^[0-9]{12}_", "", title)
            changetitle = re.sub("^[0-9]{12} ", "", changetitle)
            rename_try(title, changetitle)

        renameList = [  # 正規表現であることに注意
            [r'^＜アニメギルド＞|アニメ$', ''],
            [r'^キッズステーション$', 'KIDS'],
            [r'^TBSチャンネル$', 'TBS'],
            [r'^日テレプラス$', '日テレ'],
            [r'^BSアニマックス$', 'BS'],
            [r'^TVアニメ$', ''],
            [r'^＜夜の集中放送＞$', ''],
            [r'^【無料】$', ''],
            [r'^\[キッズステーション\]$', ''],
            [r'^テレ朝チャンネル$', 'テレ朝'],
            [r'^日テレプラス$', '日テレ'],
            [r'^TBSチャンネル$', 'TBS'],
        ]

        # renameList内の名前を置換
        for i in range(len(renameList)):
            if re.search(renameList[i], title):
                newn = renameList[i]  # [検索と置換前の名前, 置換後]
                changetitle = re.sub(newn[0], newn[1], title)
                rename_try(title, changetitle)

        if re.search("^「", title):
            changetitle = re.sub("^「", "", title)
            changetitle = re.sub("「", " ", changetitle)
            changetitle = re.sub("」", " ", changetitle)
            changetitle = re.sub("  ", " ", changetitle)
            changetitle = re.sub("   ", " ", changetitle)

            rename_try(title, changetitle,trigger)


def searchfolder(start, end, year,path,AnimeList):
    for num in range(start, end):  # path生成
        try:
            os.chdir(os.path.join(path, os.path.join(year, AnimeList[num])))
            rename()
        except WindowsError:
            pass
