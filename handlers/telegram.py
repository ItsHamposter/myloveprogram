import telebot


def send_notify(message):
    bot = telebot.TeleBot("6496435002:AAFEZbr94gdP0Uygo5BTwrA_whNjYZpAHOE")
    bot.send_message(5414925660, message)

