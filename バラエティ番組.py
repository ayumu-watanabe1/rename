import glob
import shutil
import os
import re

path="D:\\TV(h.265)\\バラエティ\\"
os.chdir(path)

print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
ans=input()
if re.search("yes",ans) or re.search("y",ans):
    delete="1"
else:
    delete="0"


def Rename():
    if(os.path.exists(new_dir_path)==False):
        os.mkdir(new_dir_path)
    try:
        shutil.move(title,new_dir_path)
    except WindowsError:
        if delete=="1":
            os.remove(title)
            print(title+"は存在するため削除しました。\n")
        else:
            print(title+"は既に存在するため処理がスキップされました。\n")

for title in glob.glob("*"+"ぴったんこカン・カン"+"*"):

    new_dir_path="D:\\TV(h.265)\\ぴったんこカン・カン\\"

    Rename()

"""for title in glob.glob("*"+"妖怪シェアハウス"+"*"):

    new_dir_path="D:\\TV(h.265)\\妖怪シェアハウス\\"

    Rename()
"""