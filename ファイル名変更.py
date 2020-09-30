import glob
import shutil
import os
import re

print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
ans=input()
if re.search("yes",ans) or re.search("y",ans):  #どちらか満たせば実行
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
            print("Error:"+title+"は既に存在するため処理がスキップされました。\n")


path="E:\\TV(h.265)\\アニメ／特撮\\"
os.chdir(path)

for title in glob.glob("*"+"さくら荘"+"*"):

    new_dir_path="E:\\TV(h.265)\\さくら荘のペットな彼女\\"
    Rename()

for title in glob.glob("*"+"転生したらスライムだった件"+"*"):

    new_dir_path="E:\\TV(h.265)\\転生したらスライムだった件\\"
    Rename()

for title in glob.glob("*"+"俺を好きなのはお前だけかよ"+"*"):

    new_dir_path="E:\\TV(h.265)\\俺を好きなのはお前だけかよ\\"
    Rename()

for title in glob.glob("*"+"月刊少女野崎くん"+"*"):

    new_dir_path="E:\\TV(h.265)\\月刊少女野崎くん\\"
    Rename()

for title in glob.glob("*"+"ソマリと森の神様"+"*"):

    new_dir_path="E:\\TV(h.265)\\ソマリと森の神様\\"
    Rename()


for title in glob.glob("*"+"ライフル・イズ・ビューティフル"+"*"):

    new_dir_path="E:\\TV(h.265)\\ライフル・イズ・ビューティフル\\"
    Rename()


for title in glob.glob("*"+"バクマン。2nd Series"+"*"):

    new_dir_path="E:\\TV(h.265)\\バクマン。(第2シリーズ)\\"
    Rename()

for title in glob.glob("*"+"バクマン。3rd Series"+"*"):

    new_dir_path="E:\\TV(h.265)\\バクマン。(第3シリーズ)\\"
    Rename()


for title in glob.glob("*"+"ぼくたちは勉強ができない!"+"*"):

    new_dir_path="E:\\TV(h.265)\\ぼくたちは勉強ができない！\\"
    Rename()

    

for title in glob.glob("*"+"アウトブレイク・カンパニー"+"*"):

    new_dir_path="E:\\TV(h.265)\\アウトブレイク・カンパニー\\"
    Rename()


for title in glob.glob("*"+"ぼくたちは勉強ができない"+"*"):

    new_dir_path="E:\\TV(h.265)\\ぼくたちは勉強ができない\\"
    Rename()


for title in glob.glob("*"+"りゅうおうのおしごと!"+"*"):

    new_dir_path="E:\\TV(h.265)\\りゅうおうのおしごと！\\"
    Rename()

   
for title in glob.glob("*"+"ソウナンですか？"+"*"):

    new_dir_path="E:\\TV(h.265)\\ソウナンですか？\\"
    Rename()

    
for title in glob.glob("*"+"生徒会役員共＊"+"*"):

    new_dir_path="E:\\TV(h.265)\\生徒会役員共＊\\"
    Rename()


for title in glob.glob("*"+"からかい上手の高木さん"+"*"):

    new_dir_path="E:\\TV(h.265)\\からかい上手の高木さん\\"
    Rename()


for title in glob.glob("*"+"五等分の花嫁"+"*"):

    new_dir_path="E:\\TV(h.265)\\五等分の花嫁\\"
    Rename()



for title in glob.glob("*"+"らき☆すたOVA"+"*"):

    new_dir_path="E:\\TV(h.265)\\らき☆すたOVA\\"
    Rename()

   

for title in glob.glob("*"+"らき☆すた"+"*"):

    new_dir_path="E:\\TV(h.265)\\らき☆すた\\"
    Rename()

   
for title in glob.glob("*"+"無彩限の"+"*"):

    new_dir_path="E:\\TV(h.265)\\無彩限のファントム・ワールド\\"
    Rename()

    

for title in glob.glob("*"+"続 夏目友人帳"+"*"):

    new_dir_path="E:\\TV(h.265)\\夏目友人帳シリーズ\\続 夏目友人帳\\"
    Rename()

    

for title in glob.glob("*"+"夏目友人帳 参"+"*"):

    new_dir_path="E:\\TV(h.265)\\夏目友人帳シリーズ\\夏目友人帳 参\\"
    Rename()

    

for title in glob.glob("*"+"夏目友人帳 肆"+"*"):

    new_dir_path="E:\\TV(h.265)\\夏目友人帳シリーズ\\夏目友人帳 肆\\"
    Rename()

    

for title in glob.glob("*"+"夏目友人帳 伍"+"*"):

    new_dir_path="E:\\TV(h.265)\\夏目友人帳シリーズ\\夏目友人帳 伍\\"
    Rename()


for title in glob.glob("*"+"夏目友人帳"+"*"):

    new_dir_path="E:\\TV(h.265)\\夏目友人帳シリーズ"
    Rename()

for title in glob.glob("*"+"けいおん!!"+"*"):

    new_dir_path="E:\\TV(h.265)\\けいおん！！\\"
    Rename()


for title in glob.glob("*"+"けいおん!"+"*"):

    new_dir_path="E:\\TV(h.265)\\けいおん！\\"
    Rename()


for title in glob.glob("*"+"デカダンス"+"*"):

    new_dir_path="E:\\TV(h.265)\\デカダンス\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"なちゅやちゅみ!+"+"*"):

    new_dir_path="E:\\TV(h.265)\\ゆるゆり なちゅやちゅみ！＋\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"なちゅやちゅみ!"+"*"):

    new_dir_path="E:\\TV(h.265)\\ゆるゆり なちゅやちゅみ！\\"
    Rename()

for title in glob.glob("*"+"ゆるゆり"+"さん☆ハイ"+"*"):

    new_dir_path="E:\\TV(h.265)\\ゆるゆり さん☆ハイ！\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"、"+"*"):

    new_dir_path="E:\\TV(h.265)\\ゆるゆり、\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"*"):

    new_dir_path="E:\\TV(h.265)\\ゆるゆり\\"
    Rename()


for title in glob.glob("*"+"ブギーポップは笑わない"+"*"):

    new_dir_path="E:\\TV(h.265)\\ブギーポップは笑わない\\"
    Rename()


for title in glob.glob("*"+"HUNTER×HUNTER"+"*"):

    new_dir_path="E:\\TV(h.265)\\HUNTER×HUNTER(2011)\\"
    Rename()

for title in glob.glob("*"+"ランウェイで笑って"+"*"):

    new_dir_path="E:\\TV(h.265)\\ランウェイで笑って\\"
    Rename()

for title in glob.glob("*"+"あの日見た花の名前"+"*"):

    new_dir_path="E:\\TV(h.265)\\あの日見た花の名前を僕達はまだ知らない。\\"
    Rename()

for title in glob.glob("*"+"ありふれた職業で"+"*"):

    new_dir_path="E:\\TV(h.265)\\ありふれた職業で世界最強\\"
    Rename()

for title in glob.glob("*"+"理系が恋に落ちた"+"*"):

    new_dir_path="E:\\TV(h.265)\\理系が恋に落ちたので証明してみた。\\"
    Rename()

for title in glob.glob("*"+"異世界チート魔術師"+"*"):

    new_dir_path="E:\\TV(h.265)\\異世界チート魔術師\\"
    Rename()

for title in glob.glob("*"+"ブギーポップは笑わない"+"*"):

    new_dir_path="E:\\TV(h.265)\\ブギーポップは笑わない\\"
    Rename()

for title in glob.glob("*"+"異種族レビュアーズ"+"*"):

    new_dir_path="E:\\TV(h.265)\\異種族レビュアーズ\\"
    Rename()

for title in glob.glob("*"+"エグゼロス"+"*"):

    new_dir_path="E:\\TV(h.265)\\ド級編隊エグゼロス\\"
    Rename()

for title in glob.glob("*"+"ピーター・グリルと"+"*"):

    new_dir_path="E:\\TV(h.265)\\ピーター・グリルと賢者の時間\\"
    Rename()

for title in glob.glob("*"+"虚構推理"+"*"):

    new_dir_path="E:\\TV(h.265)\\虚構推理\\"
    Rename()

for title in glob.glob("*"+"戦姫絶唱シンフォギアXV"+"*"):

    new_dir_path="E:\\TV(h.265)\\戦姫絶唱シンフォギアXV\\"
    Rename()

for title in glob.glob("*"+"まちカドまぞく"+"*"):

    new_dir_path="E:\\TV(h.265)\\まちカドまぞく\\"
    Rename()

for title in glob.glob("*"+"ダンベル何キロ持てる？"+"*"):

    new_dir_path="E:\\TV(h.265)\\ダンベル何キロ持てる？\\"
    Rename()

for title in glob.glob("*"+"邪神ちゃんドロップキック'"+"*"):

    new_dir_path="E:\\TV(h.265)\\邪神ちゃんドロップキック'\\"
    Rename()

for title in glob.glob("*"+"慎重勇者～この勇者が俺TUEEEくせに慎重すぎる～"+"*"):

    new_dir_path="E:\\TV(h.265)\\慎重勇者～この勇者が俺TUEEEくせに慎重すぎる～\\"
    Rename()

for title in glob.glob("*"+"彼女、お借りします"+"*"):

    new_dir_path="E:\\TV(h.265)\\彼女、お借りします\\"
    Rename()

for title in glob.glob("*"+"終物語"+"*"):

    new_dir_path="E:\\TV(h.265)\\終物語\\"
    Rename()

for title in glob.glob("*"+"憑物語"+"*"):

    new_dir_path="E:\\TV(h.265)\\憑物語\\"
    Rename()

for title in glob.glob("*"+"花子くん"+"*"):

    new_dir_path="E:\\TV(h.265)\\地縛少年花子くん\\"
    Rename()

for title in glob.glob("*"+"ヲタクに恋は難しい"+"*"):

    new_dir_path="E:\\TV(h.265)\\ヲタクに恋は難しい\\"
    Rename()

for title in glob.glob("*"+"推しが武道館"+"*"):

    new_dir_path="E:\\TV(h.265)\\推しが武道館いってくれたら死ぬ\\"
    Rename()

for title in glob.glob("*"+"神様になった日"+"*"):

    new_dir_path="E:\\TV(h.265)\\神様になった日\\"
    Rename()

for title in glob.glob("*"+"GOD EATER"+"*"):

    new_dir_path="E:\\TV(h.265)\\GOD EATER\\"
    Rename()

for title in glob.glob("*"+"ハイスコアガール"+"*"):

    new_dir_path="E:\\TV(h.265)\\ハイスコアガール\\"
    Rename()

for title in glob.glob("*"+"学園黙示録 HIGHSCHOOL"+"*"):

    new_dir_path="E:\\TV(h.265)\\学園黙示録 HIGHSCHOOL OF THE DEAD\\"
    Rename()

for title in glob.glob("*"+"CLANNAD ～AFTER STORY～"+"*"):

    new_dir_path="E:\\TV(h.265)\\CLANNAD ～AFTER STORY～\\"
    Rename()

for title in glob.glob("*"+"オーバーロードⅢ"+"*"):

    new_dir_path="E:\\TV(h.265)\\オーバーロードⅢ\\"
    Rename()

for title in glob.glob("*"+"ノラと皇女と野良猫ハート"+"*"):

    new_dir_path="E:\\TV(h.265)\\ノラと皇女と野良猫ハート\\"
    Rename()
