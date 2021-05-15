import os
import re
import function.MatchAnime as MatchAnime

delete = "0"

path = "D:\\TV(h.265)\\アニメ／特撮\\"
os.chdir(path)

basePath = 'D:/TV(h.265)'

MatchAnime.OldNameToNew(basePath, delete)
