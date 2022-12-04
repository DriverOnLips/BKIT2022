import sys
import telebot
from time import sleep
import config

test_bot = telebot.TeleBot(config.test_bot_token)


if __name__ == '__main__':
    test_bot.send_message(chat_id=config.channel_id, text='/start')
    sleep(1)
    test_bot.send_message(chat_id=config.channel_id, text='Кликер')
    sleep(1)
    test_bot.send_message(chat_id=config.channel_id, text='Клик')
    sleep(1)
    test_bot.send_message(chat_id=config.channel_id, text='клик')
    sleep(1)
    test_bot.send_message(chat_id=config.channel_id, text='Меню')
    sleep(1)
    test_bot.send_message(chat_id=config.channel_id, text='Рекорд')
    sleep(1)

    sys.exit()