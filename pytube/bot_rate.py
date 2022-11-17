import random
import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5703355736:AAEEK1seScMfcqODF_p6W3D1iJepTvJdCYc")

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Хотите узнать курс валюты?")

@bot.message_handler(commands = ['yes'])
def rate(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    rateUs = res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value']
    bot.send_message(message.chat.id, f'{rateUs}')

    # url = 'https://www.banki.ru/products/currency/cash/saratov/'
    # page = requests.get(url)
    # soup = BeautifulSoup(page.text, 'html.parser')
    # mass = soup.find_all(class_ = "table-flex__cell table-flex__cell--without-padding padding-left-default")
    # bot.send_message(message.chat.id, f'{mass}')

    # string = str(soup.find_all(class_ = "table-flex__cell table-flex__cell--without-padding padding-left-default"))
    # rateUS = string[string.find('>')+1:string.find('</div>'):].replace(',', '.')
    # bot.send_message(message.chat.id, f'{rateUS}')

bot.infinity_polling()