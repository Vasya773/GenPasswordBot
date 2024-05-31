from loader import bot
from telebot import types
import webbrowser


# @bot.message_handler(commands=['menu'])
# def main(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn_1 = types.KeyboardButton('Перейти на сайт')
#     markup.row(btn_1)
#     btn_2 = types.KeyboardButton('Узнать ID')
#     btn_3 = types.KeyboardButton('Помощь')
#     markup.row(btn_2, btn_3)
#     # bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)
#     bot.register_next_step_handler(message, register)
#
#     return markup
#
#
# def register(message):
#     if message.text == 'Перейти на сайт':
#         webbrowser.open('https://skillbox.ru')
#         bot.register_next_step_handler(message, register)
#     elif message.text == 'Узнать ID':
#         bot.send_message(message.chat.id, f'ID: {message.from_user.id}')
#         bot.register_next_step_handler(message, register)
#     elif message.text == 'Помощь':
#         bot.send_message(message.chat.id, 'Help information')
#         bot.register_next_step_handler(message, register)
#     else:
#         message_handler(message)
#
