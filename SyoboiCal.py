#しょぼいカレンダーのjsonよりアニメタイトルを取得する。

import json
import requests


def search_title(year):
    for i in range(1, 10000):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                print(json_data['Titles'][str(i)]['Title'])
                AnimeTitleList: list
                AnimeTitleList.extend(json_data['Titles'][str(i)]['Title'])
        except KeyError:
            pass

    return AnimeTitleList


url = "https://cal.syoboi.jp/json.php?Req=TitleLarge"
session = requests.Session()
data = session.get(url)
json_data = json.loads(data.text)

