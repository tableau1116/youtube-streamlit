from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Selectをインポート
from time import sleep

# Chromeオプションを設定
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # ブラウザが閉じないように設定

# ChromeDriverのサービスを設定
cService = Service(executable_path='C:\\Users\\toshi\\work\\youtube\\chromedriver.exe')
driver = webdriver.Chrome(service=cService, options=options)

# 暗黙的な待機時間を設定
driver.implicitly_wait(10)

# ログインページを開く
url_login = 'https://www.library.chiyoda.tokyo.jp/'
driver.get(url_login)

try:
    # 検索ボックスにキーワードを入力
    text_box = driver.find_element(By.NAME, 'txt_word')
    text_box.send_keys('Pythonプログラミング')

    # 検索ボタンをクリック
    btn = driver.find_element(By.NAME, 'submit_btn_searchEasy')  
    btn.click()
    
    oder = driver.find_element(By.ID,'opt_oder')
    oder_select = Select(oder)
    oder_select.select_by_value('0')
    
    btn_sort = driver.find_element(By.NAME,'submit_btn_sort')
    btn_sort.click()

    # 結果を待つ
    sleep(5)  # 必要なら明示的な待機に変更可能

except Exception as e:
    print(f"エラーが発生しました: {e}")

# スクリプト終了を防ぐ
input("終了するには Enter キーを押してください...")


#schedule_el = driver.find_elements(By.XPATH,'//li[@id="chiyoda-today-status"]/div/div')

#print([s.text for s in schedule_el])

#input("終了するには Enter キーを押してください...")
