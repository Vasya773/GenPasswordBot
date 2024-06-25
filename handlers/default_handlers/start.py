from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    """ Функция начала взаимодействия с ботом """

    bot.reply_to(message, f'Привет, {message.from_user.full_name}!\n'
                          f'Введи команду /city_user или'
                          f' /help для вызова справки')
