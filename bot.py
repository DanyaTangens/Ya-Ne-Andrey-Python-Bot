from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

TG_TOKEN = "947379327:AAGUFVQxdqdXfmid7Hsc5MJ7hhf3w3WDDIQ"


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