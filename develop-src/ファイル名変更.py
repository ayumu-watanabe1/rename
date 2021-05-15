import os
import re
import function.MatchAnime as MatchAnime

print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
ans = input()
if re.search("yes", ans) or re.search("y", ans):  # どちらか満たせば実行
    delete = "1"
else:
    delete = "0"


path = "D:\\TV(h.265)\\アニメ／特撮\\"
os.chdir(path)

basePath = 'D:/TV(h.265)'

MatchAnime.OldNameToNew(basePath,delete)
