import telebot
import os
from telebot import apihelper


apihelper.ENABLE_MIDDLEWARE = True

# initialize bot
bot = telebot.TeleBot(
    os.environ['TELEGRAMBOT_TOKEN'], parse_mode='HTML'
)
