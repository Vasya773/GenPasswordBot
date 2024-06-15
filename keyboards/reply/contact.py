from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def request_contact() -> ReplyKeyboardMarkup:
    """ Кнопка для отправки контактного номера пользователя для завершения опроса """

    keyboard = ReplyKeyboardMarkup(True, True)
    keyboard.add(KeyboardButton('Отправить контакт', request_contact=True))
    return keyboard
