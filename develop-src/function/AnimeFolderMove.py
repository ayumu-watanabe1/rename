"""
TV(h.265)内にあるアニメフォルダーを放送年に合わせて移動するプログラムである。
"""
import os
import subprocess

def foldercpy(start, end, year,oldPath,AnimeList):
    for num in range(start, end):  # path生成

        title = os.path.join(oldPath, AnimeList[num])

        if (os.path.exists(title) == True):  # ファイル・フォルダの存在確

            title2 = os.path.join(oldPath, os.path.join(year, AnimeList[num]))

            print(title+"をコピーします")
            if (os.path.isdir(title2) == False):  # ファイルが存在しない場合実行する
                try:
                    command2 = ["powershell", "-command", "New-Item",
                                '"'+title2+'"', "-Type", "Directory"]
                    subprocess.check_call(command2, shell=True)
                except:
                    pass
            try:
                command = ["powershell", "-Command", "Move-Item",
                           '"'+title+'\\*"', '"'+title2+'\\"']
                command1 = ["powershell", "-Command", "rm",
                            '"'+title+'"']
                subprocess.check_call(command, shell=True)
                subprocess.check_call(command1, shell=True)
            except:
                print("move-item error")
            # new_path = dir_util.copy_tree(title, title2)  # フォルダコピー
            # print(new_path)
            # shutil.rmtree(title)  # 元のフォルダ削除
