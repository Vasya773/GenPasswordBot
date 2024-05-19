from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = InlineKeyboardMarkup()
    btn_1 = InlineKeyboardButton('Перейти на сайт', url='https://skillbox.ru')
    markup.row(btn_1)
    btn_2 = InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn_3 = InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn_2, btn_3)
    bot.reply_to(message, f'Какое красивое фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Текст изменен', callback.message.chat.id, callback.message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()
