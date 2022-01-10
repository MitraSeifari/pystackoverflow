import telebot
import os
import telebot

# initialize bot
bot = telebot.TeleBot(
    os.environ['TELEGRAMBOT_TOKEN'], parse_mode='HTML'
)