from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def gen_markup():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text='Генерация пароля 🔑')
    button_2 = KeyboardButton(text='Угадай число 🎮')
    button_3 = KeyboardButton(text='Вызвать справку 📧')
    button_4 = KeyboardButton(text='Опрос 📝')

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard
