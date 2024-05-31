from loader import bot
from telebot.types import Message


@bot.message_handler(func=lambda message: True)
def dialogue_handler(message: Message):
    if message.text.title().startswith('Привет'):
        bot.reply_to(message, f'Рад вас снова видеть, {message.from_user.first_name}!')
    elif message.text.title().startswith('Пока'):
        bot.reply_to(message, f'Рад был с вами побеседовать, {message.from_user.first_name}!')
    elif message.text.title().startswith('Как'):
        bot.reply_to(message, f'Замечательно')
    elif message.text.title().startswith('Спасибо'):
        bot.reply_to(message, f'Рад был вам помочь, {message.from_user.first_name}!')
    else:
        bot.reply_to(message, f'Извините, я вас не понимаю. Напишите /help, чтобы получить помощь')
