from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    """ Функция вызова справки """

    text = [f'/survey - Опрос\n'
            f'/city_user - Выбрать город\n'
            f'/current_weather - Текущая погода в городе']

    bot.reply_to(message, '\n'.join(text))
