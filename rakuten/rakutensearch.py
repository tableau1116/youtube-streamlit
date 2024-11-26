import requests
import pandas as pd
APP_ID = "1027290992001933226"
KEYWORD = "ルンバ"
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"
payload = {
    "Kyword":KEYWORD,
    "applicationID":APP_ID,
    "hits":10,
    "page":1,
    "pastageFlog":1,
}

r = requests.get(url, params = payload)
r_json = r.json()


