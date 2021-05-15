"""
余計な文字列や文字を検出し削除するプログラムである。

"""
import re
from ..function import Rename_func

print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
ans = input()
if re.search("yes", ans) or re.search("y", ans):
    delete = "1"
else:
    delete = "0"

path1 = 'H:/TV(h.265)'
path2 = 'D:/TV(h.265)/映画'
path3 = 'D:/TV(h.265)/夏目友人帳シリーズ/夏目友人帳'
path4 = 'D:/TV(h.265)/夏目友人帳シリーズ/夏目友人帳 陸'
path5 = 'D:/TV(h.265)/夏目友人帳シリーズ/続 夏目友人帳'
path6 = 'D:/TV(h.265)/ANIMAX MUSIX'

Rename_func.rename(delete)

openPath = '/dataset/'
startYear, endYear = 1999, 2021

for i in range(endYear - startYear + 1):
    with open(openPath+str(startYear+i)+'.txt', encoding="utf-8") as f:
        AnimeList = [s.strip() for s in f.readlines()]
        try:
            Rename_func.searchfolder(
                0, 150, str(startYear + i), path1, AnimeList)
                
        except:  # この書き方は公式でもあまり推奨されません..
            pass
