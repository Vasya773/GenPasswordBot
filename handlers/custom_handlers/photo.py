from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    """ Функция получения и реагирования на фото от пользователя """

    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('Удалить фото', callback_data='delete')
    markup.row(btn)
    bot.reply_to(message, f'Какое красивое фото!\nНажми /help чтобы продолжить', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    """ Функция удаления последнего фото """

    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
