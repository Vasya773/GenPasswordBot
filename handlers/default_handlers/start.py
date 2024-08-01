from loader import bot
from telebot.types import Message
from keyboards.reply.start_reply import gen_markup


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    """ Функция начала взаимодействия с ботом """

    bot.reply_to(message, "Привет! Я могу сгенерировать случайный пароль для вас. "
                          "Введите команду '/generate <длина пароля>' для генерации пароля.\n\n"
                          "Также вы можете сыграть в игру 'Угадай число' с помощью команды /play.",
                 reply_markup=gen_markup())
