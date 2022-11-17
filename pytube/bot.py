import random
import telebot
import time
from pytube import YouTube

bot = telebot.TeleBot("5703355736:AAEEK1seScMfcqODF_p6W3D1iJepTvJdCYc")

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Отправь ссылку на видео")

@bot.message_handler(func = lambda message: True)
def video_dwnld(message):
    chat_id = message.chat.id

    yt = YouTube(message.text)
    yt.streams.filter(res="144p").first().download(filename = f"{chat_id}.mp4")

    bot.send_video(chat_id, video = open(f"{chat_id}.mp4", 'rb'), supports_streaming = True)
    print(yt.title)

bot.infinity_polling()