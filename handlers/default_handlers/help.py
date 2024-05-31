from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    text = [f'/survey - Опрос']

    bot.reply_to(message, '\n'.join(text))
