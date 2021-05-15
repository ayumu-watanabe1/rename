"""
    大学の講義毎に授業回数分ファイルを作成するプログラム
    例）社会学A----第1回‐--指定したファイル.txt
                  -第2回‐--指定したファイル.txt
                  -第3回‐--指定したファイル.txt
"""

import os
import shutil
import re

print("作成する場所を入力してください。例) c:\\Users")

path=input()

print("講義の名称は何ですか？\n")

title=input()

print("全講義の授業回数は何回ですか？数字で入力してください。\n")

number=int(input())

#実装中
"""print("講義回数全てに特定のファイルをコピーしますか？ yes/no\n") 
ans=input()
if re.search("yes",ans) or re.search("y",ans):
    flag=1
    print("コピーするファイルの元を指定してください\n")
    Cpy_file=input()
else:
    flag=0
"""
print(title+"の講義名以下に"+str(number)+"回分のフォルダを作成します。\n")

path1=os.path.join(path,title)
try:
    os.mkdir(path1)
    print(path1+"を作成しました。\n")

except WindowsError:    #存在している場合のエラー処理
    print(path1+"は既に存在しています\n")


for num in range(1,number+1):
    new_path=os.path.join(path1,"第"+str(num)+"回")

    #実装中
    """if flag==1:
        try:
            temp=os.path.basename(Cpy_file)
            shutil.copyfile(Cpy_file,os.path.join(new_path,Cpy_file))
        except WindowsError:
            print(temp+"ファイルはすでに存在しています。\n")
            """

    try:
        os.mkdir(new_path)
        print(new_path+"を作成しました。\n")
    except WindowsError:
        print(new_path+"はすでに存在しています。\n")