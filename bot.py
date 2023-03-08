import telebot
from sys import exit
from os import environ

BOT_TOKEN = environ.get('BOT_TOKEN')
CHAT_ID = ""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "start")
    
@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, "hello !!!")
    bot.send_message(message.chat.id,"how are you ?")
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message,message.text)

print("[ OK ] - Bot is serving infinitly...")
bot.infinity_polling()
