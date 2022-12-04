import config
import telebot
import sys

bot = telebot.TeleBot(config.bot_token)
NUM = 0
TOP = 0


# start handler
@bot.channel_post_handler(commands=["start"])
def start_message(message):
    global NUM, TOP
    NUM = TOP = 0
    text = 'Добро пожаловать! Для игры напиши "Кликер", для информации о рекорде напиши "Рекорд"'
    bot.send_message(message.chat.id, text=text)


# clicker handler
@bot.channel_post_handler(func=lambda message: message.text == 'Кликер' or message.text == 'кликер')
def clicker_message(message):
    text = 'Пиши слово "Клик" как можно быстрее!'
    bot.send_message(message.chat.id, text=text)


# record handler
@bot.channel_post_handler(func=lambda message: message.text == 'Рекорд' or message.text == 'рекорд')
def clicker_message(message):
    global TOP
    if TOP == 0:
        result = "Ты еще не играл!"
    else:
        if TOP % 10 == 1 and TOP not in [11, 12, 13, 14]:
            click = "клик"
        elif 2 <= TOP % 10 <= 4 and TOP not in [11, 12, 13, 14]:
            click = "клика"
        else:
            click = "кликов"
        result = f"Твой лучший результат {TOP} {click}."
    text = f'{result} Чтобы вернуться в меню, напиши "/start"'
    bot.send_message(message.chat.id, text=text)


# click handler
@bot.channel_post_handler(func=lambda message: message.text == 'Клик' or message.text == 'клик')
def click_handler(message):
    global NUM
    NUM += 1
    if NUM == 1:
        text = "клик"
    elif 2 <= NUM <= 4:
        text = "клика"
    else:
        text = "кликов"
    bot.send_message(message.chat.id, text=f'Вау, у тебя уже {NUM} {text}. Продолжай писать "Клик" и '
                                           f'дальше. Но если хочешь вернуться назад, напиши "Меню"')


# menu handler
@bot.channel_post_handler(func=lambda message: message.text == 'Меню' or message.text == 'меню')
def click_handler(message):
    global NUM, TOP
    if TOP < NUM: TOP = NUM
    NUM = 0
    text = 'Для игры напиши "Кликер", для информации о рекорде напиши "Рекорд"'
    bot.send_message(message.chat.id, text=text)


# exit handler
@bot.channel_post_handler(func=lambda message: message.text == 'exit' or message.text == 'Exit')
def bot_exit():
    sys.exit(0)
    print(1)


# unknown handler
@bot.channel_post_handler(content_types=["text"])
def unknown_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, text='Напиши "/start"')


bot.polling()

bot.send_message(chat_id=config.channel_id, text='/start')
