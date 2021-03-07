import glob
import shutil
import os
import re

#print("これからファイルを移動しますが、既に存在した場合　削除　しますか？ yesかnoで\n")
delete = "0"


def Rename():
    if(os.path.exists(new_dir_path) == False):
        os.mkdir(new_dir_path)
    try:
        shutil.move(title, new_dir_path)
    except WindowsError:
        if delete == "1":
            os.remove(title)
            print(title+"は存在するため削除しました。\n")
        else:
            print("Error:"+title+"は既に存在するため処理がスキップされました。\n")


path = "E:\\TV\\アニメ／特撮\\"
os.chdir(path)

for title in glob.glob("*"+"さくら荘"+"*"):

    new_dir_path = "E:\\TV\\さくら荘のペットな彼女\\"
    Rename()

for title in glob.glob("*"+"転生したらスライムだった件"+"*"):

    new_dir_path = "E:\\TV\\転生したらスライムだった件\\"
    Rename()

for title in glob.glob("*"+"俺を好きなのはお前だけかよ"+"*"):

    new_dir_path = "E:\\TV\\俺を好きなのはお前だけかよ\\"
    Rename()

for title in glob.glob("*"+"月刊少女野崎くん"+"*"):

    new_dir_path = "E:\\TV\\月刊少女野崎くん\\"
    Rename()

for title in glob.glob("*"+"ソマリと森の神様"+"*"):

    new_dir_path = "E:\\TV\\ソマリと森の神様\\"
    Rename()


for title in glob.glob("*"+"ライフル・イズ・ビューティフル"+"*"):

    new_dir_path = "E:\\TV\\ライフル・イズ・ビューティフル\\"
    Rename()


for title in glob.glob("*"+"バクマン。1st Series"+"*"):

    new_dir_path = "E:\\TV\\バクマン。(第1シリーズ)\\"
    Rename()

for title in glob.glob("*"+"バクマン。2nd Series"+"*"):

    new_dir_path = "E:\\TV\\バクマン。(第2シリーズ)\\"
    Rename()

for title in glob.glob("*"+"バクマン。3rd Series"+"*"):

    new_dir_path = "E:\\TV\\バクマン。(第3シリーズ)\\"
    Rename()


for title in glob.glob("*"+"ぼくたちは勉強ができない!"+"*"):

    new_dir_path = "E:\\TV\\ぼくたちは勉強ができない！\\"
    Rename()


for title in glob.glob("*"+"アウトブレイク・カンパニー"+"*"):

    new_dir_path = "E:\\TV\\アウトブレイク・カンパニー\\"
    Rename()


for title in glob.glob("*"+"ぼくたちは勉強ができない"+"*"):

    new_dir_path = "E:\\TV\\ぼくたちは勉強ができない\\"
    Rename()


for title in glob.glob("*"+"りゅうおうのおしごと!"+"*"):

    new_dir_path = "E:\\TV\\りゅうおうのおしごと！\\"
    Rename()


for title in glob.glob("*"+"ソウナンですか？"+"*"):

    new_dir_path = "E:\\TV\\ソウナンですか？\\"
    Rename()


for title in glob.glob("*"+"生徒会役員共＊"+"*"):

    new_dir_path = "E:\\TV\\生徒会役員共＊\\"
    Rename()


for title in glob.glob("*"+"からかい上手の高木さん"+"*"):

    new_dir_path = "E:\\TV\\からかい上手の高木さん\\"
    Rename()


for title in glob.glob("*"+"五等分の花嫁"+"*"):

    new_dir_path = "E:\\TV\\五等分の花嫁\\"
    Rename()


for title in glob.glob("*"+"らき☆すたOVA"+"*"):

    new_dir_path = "E:\\TV\\らき☆すたOVA\\"
    Rename()


for title in glob.glob("*"+"らき☆すた"+"*"):

    new_dir_path = "E:\\TV\\らき☆すた\\"
    Rename()


for title in glob.glob("*"+"無彩限の"+"*"):

    new_dir_path = "E:\\TV\\無彩限のファントム・ワールド\\"
    Rename()


for title in glob.glob("*"+"続 夏目友人帳"+"*"):

    new_dir_path = "E:\\TV\\夏目友人帳シリーズ\\続 夏目友人帳\\"
    Rename()


for title in glob.glob("*"+"夏目友人帳 参"+"*"):

    new_dir_path = "E:\\TV\\夏目友人帳シリーズ\\夏目友人帳 参\\"
    Rename()


for title in glob.glob("*"+"夏目友人帳 肆"+"*"):

    new_dir_path = "E:\\TV\\夏目友人帳シリーズ\\夏目友人帳 肆\\"
    Rename()


for title in glob.glob("*"+"夏目友人帳 伍"+"*"):

    new_dir_path = "E:\\TV\\夏目友人帳シリーズ\\夏目友人帳 伍\\"
    Rename()


for title in glob.glob("*"+"夏目友人帳"+"*"):

    new_dir_path = "E:\\TV\\夏目友人帳シリーズ"
    Rename()

for title in glob.glob("*"+"けいおん!!"+"*"):

    new_dir_path = "E:\\TV\\けいおん！！\\"
    Rename()


for title in glob.glob("*"+"けいおん!"+"*"):

    new_dir_path = "E:\\TV\\けいおん！\\"
    Rename()


for title in glob.glob("*"+"デカダンス"+"*"):

    new_dir_path = "E:\\TV\\デカダンス\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"なちゅやちゅみ!+"+"*"):

    new_dir_path = "E:\\TV\\ゆるゆり なちゅやちゅみ！＋\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"なちゅやちゅみ!"+"*"):

    new_dir_path = "E:\\TV\\ゆるゆり なちゅやちゅみ！\\"
    Rename()

for title in glob.glob("*"+"ゆるゆり"+"さん☆ハイ"+"*"):

    new_dir_path = "E:\\TV\\ゆるゆり さん☆ハイ！\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"、"+"*"):

    new_dir_path = "E:\\TV\\ゆるゆり、\\"
    Rename()


for title in glob.glob("*"+"ゆるゆり"+"*"):

    new_dir_path = "E:\\TV\\ゆるゆり\\"
    Rename()


for title in glob.glob("*"+"ブギーポップは笑わない"+"*"):

    new_dir_path = "E:\\TV\\ブギーポップは笑わない\\"
    Rename()


for title in glob.glob("*"+"HUNTER×HUNTER"+"*"):

    new_dir_path = "E:\\TV\\HUNTER×HUNTER(2011)\\"
    Rename()

for title in glob.glob("*"+"ランウェイで笑って"+"*"):

    new_dir_path = "E:\\TV\\ランウェイで笑って\\"
    Rename()

for title in glob.glob("*"+"あの日見た花の名前"+"*"):

    new_dir_path = "E:\\TV\\あの日見た花の名前を僕達はまだ知らない。\\"
    Rename()

for title in glob.glob("*"+"ありふれた職業で"+"*"):

    new_dir_path = "E:\\TV\\ありふれた職業で世界最強\\"
    Rename()

for title in glob.glob("*"+"理系が恋に落ちた"+"*"):

    new_dir_path = "E:\\TV\\理系が恋に落ちたので証明してみた。\\"
    Rename()

for title in glob.glob("*"+"異世界チート魔術師"+"*"):

    new_dir_path = "E:\\TV\\異世界チート魔術師\\"
    Rename()

for title in glob.glob("*"+"ブギーポップは笑わない"+"*"):

    new_dir_path = "E:\\TV\\ブギーポップは笑わない\\"
    Rename()

for title in glob.glob("*"+"異種族レビュアーズ"+"*"):

    new_dir_path = "E:\\TV\\異種族レビュアーズ\\"
    Rename()

for title in glob.glob("*"+"エグゼロス"+"*"):

    new_dir_path = "E:\\TV\\ド級編隊エグゼロス\\"
    Rename()

for title in glob.glob("*"+"ピーター・グリルと"+"*"):

    new_dir_path = "E:\\TV\\ピーター・グリルと賢者の時間\\"
    Rename()

for title in glob.glob("*"+"虚構推理"+"*"):

    new_dir_path = "E:\\TV\\虚構推理\\"
    Rename()

for title in glob.glob("*"+"戦姫絶唱シンフォギアXV"+"*"):

    new_dir_path = "E:\\TV\\戦姫絶唱シンフォギアXV\\"
    Rename()

for title in glob.glob("*"+"まちカドまぞく"+"*"):

    new_dir_path = "E:\\TV\\まちカドまぞく\\"
    Rename()

for title in glob.glob("*"+"ダンベル何キロ持てる？"+"*"):

    new_dir_path = "E:\\TV\\ダンベル何キロ持てる？\\"
    Rename()

for title in glob.glob("*"+"邪神ちゃんドロップキック'"+"*"):

    new_dir_path = "E:\\TV\\邪神ちゃんドロップキック'\\"
    Rename()

for title in glob.glob("*"+"慎重勇者～この勇者が俺TUEEEくせに慎重すぎる～"+"*"):

    new_dir_path = "E:\\TV\\慎重勇者～この勇者が俺TUEEEくせに慎重すぎる～\\"
    Rename()

for title in glob.glob("*"+"彼女、お借りします"+"*"):

    new_dir_path = "E:\\TV\\彼女、お借りします\\"
    Rename()

for title in glob.glob("*"+"終物語"+"*"):

    new_dir_path = "E:\\TV\\終物語\\"
    Rename()

for title in glob.glob("*"+"憑物語"+"*"):

    new_dir_path = "E:\\TV\\憑物語\\"
    Rename()

for title in glob.glob("*"+"花子くん"+"*"):

    new_dir_path = "E:\\TV\\地縛少年花子くん\\"
    Rename()

for title in glob.glob("*"+"ヲタクに恋は難しい"+"*"):

    new_dir_path = "E:\\TV\\ヲタクに恋は難しい\\"
    Rename()

for title in glob.glob("*"+"推しが武道館"+"*"):

    new_dir_path = "E:\\TV\\推しが武道館いってくれたら死ぬ\\"
    Rename()

for title in glob.glob("*"+"神様になった日"+"*"):

    new_dir_path = "E:\\TV\\神様になった日\\"
    Rename()

for title in glob.glob("*"+"GOD EATER"+"*"):

    new_dir_path = "E:\\TV\\GOD EATER\\"
    Rename()

for title in glob.glob("*"+"ハイスコアガール"+"*"):

    new_dir_path = "E:\\TV\\ハイスコアガール\\"
    Rename()

for title in glob.glob("*"+"学園黙示録 HIGHSCHOOL"+"*"):

    new_dir_path = "E:\\TV\\学園黙示録 HIGHSCHOOL OF THE DEAD\\"
    Rename()

for title in glob.glob("*"+"CLANNAD ～AFTER STORY～"+"*"):

    new_dir_path = "E:\\TV\\CLANNAD ～AFTER STORY～\\"
    Rename()

for title in glob.glob("*"+"オーバーロードⅢ"+"*"):

    new_dir_path = "E:\\TV\\オーバーロードIII\\"
    Rename()

for title in glob.glob("*"+"ノラと皇女と野良猫ハート"+"*"):

    new_dir_path = "E:\\TV\\ノラと皇女と野良猫ハート\\"
    Rename()

for title in glob.glob("*"+"胡蝶綺 ～若き信長～"+"*"):

    new_dir_path = "E:\\TV\\胡蝶綺 ～若き信長～\\"
    Rename()

for title in glob.glob("*"+"バジャのスタジオ～バジャのみた海～"+"*"):

    new_dir_path = "E:\\TV\\バジャのスタジオ～バジャのみた海～\\"
    Rename()

for title in glob.glob("*"+"上野さんは不器用"+"*"):

    new_dir_path = "E:\\TV\\上野さんは不器用\\"
    Rename()

for title in glob.glob("*"+"あそびあそばせ"+"*"):

    new_dir_path = "E:\\TV\\あそびあそばせ\\"
    Rename()

for title in glob.glob("*"+"へやキャン△"+"*"):

    new_dir_path = "E:\\TV\\へやキャン△\\"
    Rename()

for title in glob.glob("*"+"Lapis Re：LiGHTs"+"*"):

    new_dir_path = "E:\\TV\\Lapis Re：LiGHTs ラピスリライツ\\"
    Rename()

for title in glob.glob("*"+"となりの吸血鬼さん"+"*"):

    new_dir_path = "E:\\TV\\となりの吸血鬼さん\\"
    Rename()

for title in glob.glob("*"+"NOBLESSE -ノブレス-"+"*"):

    new_dir_path = "E:\\TV\\NOBLESSE -ノブレス-\\"
    Rename()

for title in glob.glob("*"+"犬夜叉 完結編"+"*"):

    new_dir_path = "E:\\TV\\犬夜叉 完結編\\"
    Rename()

for title in glob.glob("*"+"織田信奈の野望"+"*"):

    new_dir_path = "E:\\TV\\織田信奈の野望\\"
    Rename()

for title in glob.glob("*"+"OVA かのこん～真夏の大謝肉祭～"+"*"):

    new_dir_path = "E:\\TV\\かのこん ～真夏の大謝肉祭～\\"
    Rename()

for title in glob.glob("*"+"聖痕のクェイサーII"+"*"):

    new_dir_path = "E:\\TV\\聖痕のクェイサーII\\"
    Rename()

for title in glob.glob("*"+"世話やきキツネの仙狐さん"+"*"):

    new_dir_path = "E:\\TV\\世話やきキツネの仙狐さん\\"
    Rename()

for title in glob.glob("*"+"痛いのは嫌なので防御力に極振りしたいと思います。"+"*"):

    new_dir_path = "E:\\TV\\痛いのは嫌なので防御力に極振りしたいと思います。\\"
    Rename()

for title in glob.glob("*"+"八男って、それはないでしょう"+"*"):

    new_dir_path = "E:\\TV\\八男って、それはないでしょう！\\"
    Rename()

for title in glob.glob("*"+"くまクマ熊ベアー"+"*"):

    new_dir_path = "E:\\TV\\くまクマ熊ベアー\\"
    Rename()

for title in glob.glob("*"+"100万の命の上に俺は立っている"+"*"):

    new_dir_path = "E:\\TV\\100万の命の上に俺は立っている\\"
    Rename()

for title in glob.glob("*"+"いわかける!"+"*"):

    new_dir_path = "E:\\TV\\いわかける！ -Sport Climbing Girls-\\"
    Rename()

for title in glob.glob("*"+"アクダマドライブ"+"*"):

    new_dir_path = "E:\\TV\\アクダマドライブ\\"
    Rename()

for title in glob.glob("*"+"キングスレイド 意志を継ぐものたち"+"*"):

    new_dir_path = "E:\\TV\\キングスレイド 意志を継ぐものたち\\"
    Rename()

for title in glob.glob("*"+"鬼滅の刃"+"*"):

    new_dir_path = "E:\\TV\\鬼滅の刃\\"
    Rename()

for title in glob.glob("*"+"かぐや様は告らせたい～天才たちの恋愛頭脳戦～"+"*"):

    new_dir_path = "E:\\TV\\かぐや様は告らせたい～天才たちの恋愛頭脳戦～\\"
    Rename()

for title in glob.glob("*"+"ANIMAX MUSIX"+"*"):

    new_dir_path = "E:\\TV\\ANIMAX MUSIX\\"
    Rename()

for title in glob.glob("*"+"ガーリー・エアフォース"+"*"):

    new_dir_path = "E:\\TV\\ガーリー・エアフォース\\"
    Rename()

for title in glob.glob("*"+"体操ザムライ"+"*"):

    new_dir_path = "E:\\TV\\体操ザムライ\\"
    Rename()

for title in glob.glob("*"+"トニカクカワイイ"+"*"):

    new_dir_path = "E:\\TV\\トニカクカワイイ\\"
    Rename()

for title in glob.glob("*"+"やはり俺の青春ラブコメはまちがっている。完"+"*"):

    new_dir_path = "E:\\TV\\やはり俺の青春ラブコメはまちがっている。完\\"
    Rename()

for title in glob.glob("*"+"異能バトルは日常系のなかで"+"*"):

    new_dir_path = "E:\\TV\\異能バトルは日常系のなかで\\"
    Rename()

for title in glob.glob("*"+"Re：ゼロから始める異世界生活 氷結の絆"+"*"):

    new_dir_path = "E:\\TV\\Re：ゼロから始める異世界生活 氷結の絆\\"
    Rename()

for title in glob.glob("*"+"デート・ア・ライブ"+"*"):

    new_dir_path = "E:\\TV\\デート・ア・ライブ\\"
    Rename()

for title in glob.glob("*"+"アサシンズプライド"+"*"):

    new_dir_path = "E:\\TV\\アサシンズプライド\\"
    Rename()

for title in glob.glob("*"+"魔王様、リトライ"+"*"):

    new_dir_path = "E:\\TV\\魔王様、リトライ\\"
    Rename()

for title in glob.glob("*"+"戦×恋(ヴァルラヴ)"+"*"):

    new_dir_path = "E:\\TV\\戦×恋(ヴァルラヴ)\\"
    Rename()

for title in glob.glob("*"+"アホガール"+"*"):

    new_dir_path = "E:\\TV\\アホガール\\"
    Rename()

for title in glob.glob("*"+"中二病でも恋がしたい！"+"*"):

    new_dir_path = "E:\\TV\\中二病でも恋がしたい！\\"
    Rename()

for title in glob.glob("*"+"ゆるキャン△"+"*"):

    new_dir_path = "E:\\TV\\ゆるキャン△\\"
    Rename()

for title in glob.glob("*"+"結界師"+"*"):

    new_dir_path = "E:\\TV\\結界師\\"
    Rename()

for title in glob.glob("*"+"ヨスガノソラ"+"*"):

    new_dir_path = "E:\\TV\\ヨスガノソラ\\"
    Rename()

for title in glob.glob("*"+"フェアリーゴーン"+"*"):

    new_dir_path = "E:\\TV\\Fairy gone フェアリーゴーン\\"
    Rename()

for title in glob.glob("*"+"政宗くんのリベンジ"+"*"):

    new_dir_path = "E:\\TV\\政宗くんのリベンジ\\"
    Rename()

for title in glob.glob("*"+"キミと僕の最後の戦場、あるいは世界が始まる聖戦"+"*"):

    new_dir_path = "E:\\TV\\キミと僕の最後の戦場、あるいは世界が始まる聖戦\\"
    Rename()

for title in glob.glob("*"+"日曜アニメ劇場"+"*"):

    new_dir_path = "E:\\TV\\日曜アニメ劇場\\"
    Rename()

for title in glob.glob("*"+"トクナナ"+"*"):

    new_dir_path = "E:\\TV\\警視庁 特務部 特殊凶悪犯対策室 第七課 -トクナナ-\\"
    Rename()

for title in glob.glob("*"+"賢者の孫"+"*"):

    new_dir_path = "E:\\TV\\賢者の孫\\"
    Rename()

for title in glob.glob("*"+"トリニティセブン"+"*"):

    new_dir_path = "E:\\TV\\トリニティセブン\\"
    Rename()

for title in glob.glob("*"+"うちのメイドがウザすぎる"+"*"):

    new_dir_path = "E:\\TV\\うちのメイドがウザすぎる!\\"
    Rename()

for title in glob.glob("*"+"バカとテストと召喚獣にっ"+"*"):

    new_dir_path = "E:\\TV\\バカとテストと召喚獣にっ!\\"
    Rename()

for title in glob.glob("*"+"涼宮ハルヒの憂鬱"+"*"):

    new_dir_path = "E:\\TV\\涼宮ハルヒの憂鬱\\"
    Rename()

for title in glob.glob("*"+"なんでここに先生が"+"*"):

    new_dir_path = "E:\\TV\\なんでここに先生が！？\\"
    Rename()

for title in glob.glob("*"+"聖痕のクェイサー"+"*"):

    new_dir_path = "E:\\TV\\聖痕のクェイサー\\"
    Rename()

for title in glob.glob("*"+"アサルトリリィ"+"*"):

    new_dir_path = "E:\\TV\\アサルトリリィ BOUQUET\\"
    Rename()

for title in glob.glob("*"+"中二病でも恋がしたい!戀"+"*"):

    new_dir_path = "E:\\TV\\中二病でも恋がしたい！戀\\"
    Rename()

for title in glob.glob("*"+"中二病でも恋がしたい!"+"*"):

    new_dir_path = "E:\\TV\\中二病でも恋がしたい！\\"
    Rename()

for title in glob.glob("*"+"繰繰れ! コックリさん"+"*"):

    new_dir_path = "E:\\TV\\繰繰れ！コックリさん\\"
    Rename()

for title in glob.glob("*"+"甘々と稲妻"+"*"):

    new_dir_path = "E:\\TV\\甘々と稲妻\\"
    Rename()

for title in glob.glob("*"+"WHITE ALBUM"+"*"):

    new_dir_path = "E:\\TV\\WHITE ALBUM\\"
    Rename()

for title in glob.glob("*"+"ダーウィンズゲーム"+"*"):

    new_dir_path = "E:\\TV\\ダーウィンズゲーム\\"
    Rename()

for title in glob.glob("*"+"衛宮さんちの今日のごはん"+"*"):

    new_dir_path = "E:\\TV\\衛宮さんちの今日のごはん\\"
    Rename()

for title in glob.glob("*"+"デスマーチからはじまる異世界狂想曲"+"*"):

    new_dir_path = "E:\\TV\\デスマーチからはじまる異世界狂想曲\\"
    Rename()

for title in glob.glob("*"+"刀使ノ巫女"+"*"):

    new_dir_path = "E:\\TV\\刀使ノ巫女\\"
    Rename()

for title in glob.glob("*"+"金曜ロードSHOW!"+"*"):

    new_dir_path = "E:\\TV\\金曜ロードSHOW！\\"
    Rename()

for title in glob.glob("*"+"おちこぼれフルーツタルト"+"*"):

    new_dir_path = "E:\\TV\\おちこぼれフルーツタルト\\"
    Rename()

for title in glob.glob("*"+"池袋ウエストゲートパーク"+"*"):

    new_dir_path = "E:\\TV\\池袋ウエストゲートパーク\\"
    Rename()

for title in glob.glob("*"+"さよならの朝に約束の花をかざろう"+"*"):

    new_dir_path = "E:\\TV\\さよならの朝に約束の花をかざろう\\"
    Rename()

for title in glob.glob("*"+"憂国のモリアーティ"+"*"):

    new_dir_path = "E:\\TV\\憂国のモリアーティ\\"
    Rename()

for title in glob.glob("*"+"ひとりぼっちの○○生活"+"*"):

    new_dir_path = "E:\\TV\\ひとりぼっちの○○生活\\"
    Rename()

for title in glob.glob("*"+"舟を編む"+"*"):

    new_dir_path = "E:\\TV\\舟を編む\\"
    Rename()

for title in glob.glob("*"+"revisions"+"*"):

    new_dir_path = "E:\\TV\\revisions\\"
    Rename()

for title in glob.glob("*"+"僕らはみんな河合荘"+"*"):

    new_dir_path = "E:\\TV\\僕らはみんな河合荘\\"
    Rename()

for title in glob.glob("*"+"文豪ストレイドッグス"+"*"):

    new_dir_path = "E:\\TV\\文豪ストレイドッグス\\"
    Rename()
