"""
余計な文字列や文字を検出し削除するプログラムである。

"""
import re
import function.Rename_func as Rename_func

path1 = 'E:/TV'
# path1=r"D:\TV_data"

delete = "0"

# delete=1   :重複したら削除する
# delete=0   :重複したら削除しない

path2 = 'D:/TV(h.265)/映画'
path3 = 'D:/TV(h.265)/夏目友人帳シリーズ/夏目友人帳'
path4 = 'D:/TV(h.265)/夏目友人帳シリーズ/夏目友人帳 陸'
path5 = 'D:/TV(h.265)/夏目友人帳シリーズ/続 夏目友人帳'
path6 = 'D:/TV(h.265)/ANIMAX MUSIX'

Rename_func.rename(delete)

openPath = 'F:/git/rename/dataset/'
startYear, endYear = 1999, 2021

for i in range(endYear - startYear + 1):
    with open(openPath+str(startYear+i)+'.txt', encoding="utf-8") as f:
        AnimeList = [s.strip() for s in f.readlines()]
        try:
            Rename_func.searchfolder(
                0, 150, str(startYear + i), path1, AnimeList)

        except:  # この書き方は公式でもあまり推奨されません..
            pass
