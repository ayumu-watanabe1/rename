"""
TV(h.265)内にあるアニメフォルダーを放送年に合わせて移動するプログラムである。
"""
import function.AnimeFolderMove as AnimeFolderMove

path1 = 'D:/TV(h.265)'

openPath = 'F:/git/rename/dataset/'
startYear, endYear = 1999, 2021

for i in range(endYear - startYear + 1):
    with open(openPath+str(startYear+i)+'.txt', encoding="utf-8") as f:
        AnimeList = [s.strip() for s in f.readlines()]
    try:
        AnimeFolderMove.foldercpy(0, 1000, str(startYear+i),path1,AnimeList)
    except:
        pass
