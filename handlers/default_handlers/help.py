from loader import bot
from telebot.types import Message


@bot.message_handler(func=lambda message: message.text == 'Вызвать справку 📧')
def bot_help(message: Message):
    """ Функция вызова справки """

    text = [f'Введите /generate (длина пароля) - Генерация пароля\n'
            f'/play - Угадай число\n'
            f'/survey - Опрос\n'
            f'Можете отправить любое фото боту, он оценит']

    bot.reply_to(message, '\n'.join(text))


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    """ Функция вызова справки """

    text = [f'Введите /generate (длина пароля) - Генерация пароля\n'
            f'/play - Угадай число\n'
            f'/survey - Опрос\n'
            f'Можете отправить любое фото боту, он оценит']

    bot.reply_to(message, '\n'.join(text))
