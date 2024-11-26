import requests
import pandas as ps
REQUEST_URL = 'https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426'
APP_ID = '1027290992001933226'
params = {
    'format':'jason',
    'largeClassCode':'japan',
    'middleClassCode':'okinawa',
    'smallClassCode':'nakashi',
    'applicationId': APP_ID
}
res = requests.get(REQUEST_URL, params)
result = res.json()
result