"""
TV(h.265)内にあるアニメフォルダーを放送年に合わせて移動するプログラムである。
"""
import function.AnimeFolderMove as AnimeFolderMove

path1 = 'E:/TV'
#path1 = "D:\\TV_data"

openPath = 'F:/git/rename/dataset/'
startYear, endYear = 1999, 2021

for i in range(endYear - startYear + 1):
    with open(openPath+str(startYear+i)+'.txt', encoding="utf-8") as f:
        l = [s.strip() for s in f.readlines()]
    try:
        AnimeFolderMove.foldercpy(0, 500, str(startYear+i))
    except:
        pass
