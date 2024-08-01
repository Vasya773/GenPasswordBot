from loader import bot
from telebot.types import Message


@bot.message_handler(func=lambda message: True)
def dialogue_handler(message: Message) -> None:
    """ Функция диалога с пользователем """

    bot.reply_to(message, f"Извините, я вас не понимаю.\n"
                          f"Введите команду '/generate <длина пароля>' или\n"
                          f"/help для вызова справки")
