import os
import re
import function.MatchAnime as MatchAnime

#print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
delete = "0"

path = "E:\\TV\\アニメ／特撮\\"
os.chdir(path)

basePath = 'E:/TV/'

MatchAnime.OldNameToNew(basePath, delete)
