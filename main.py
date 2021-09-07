import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
from collections import OrderedDict
import traceback
import sys
import telebot
from datetime import datetime, timedelta
#20.06.2021 18:48 Güncelleme

temp = str()
temp_value = float()
Bot_Token = "1712159334:AAGwq25dFU_YjbVG9fuiM_6DwV16oG1JEX8"
Chat_ID = "-1001435277863"
TradeBot = telebot.TeleBot(Bot_Token)

def SendToTelegram(message):
    requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendMessage?chat_id=" + Chat_ID + "&text=" + message)

whale = list()
whale = list()
driver = webdriver.Chrome()
url = f"https://whale-alert.io/"
driver.get(url)
time.sleep(3)

while True:

    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, "html.parser")
    whale_alert = soup.find_all("span","tx")
    usd_amount = soup.find_all("span","tx-usd-amount")
    for i in whale_alert:
        i = i.text
        whale.append(i)
    for j in usd_amount:
        j = j.text
        j = j[1:-5]
        j = re.sub('[!@#$,]', '', j)
        whale_alert.append(j)

    if temp != whale[-2] and float(whale_alert[-1]) >= 100000:

        message = whale[-2][9:]
        SendToTelegram(message)
    temp = whale[-2]
    temp_value = whale_alert[-2]
