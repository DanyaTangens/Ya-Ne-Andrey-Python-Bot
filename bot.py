from telegram import Bot
from telegram import Update
import urllib.request, json
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import json, re, requests


TG_TOKEN = "your token"


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'аноним'
    
    text = update.effective_message.text
    reply_text = f'Здарова, {name}!\n\n{text}'

    bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = reply_text,
    )

def anekdot(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Челядь'
    
    request = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1")
    response = request.text
    response = response.replace("\n","")
    response = response.replace("\r","")
    text = json.loads(response)

    reply_text = f'{name}, слушай анекдот\n {text}'

    bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = reply_text,
    ) 


def main():
    bot = Bot(
        token = TG_TOKEN    
    )
    updater = Updater(
        bot=bot,
    )

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
