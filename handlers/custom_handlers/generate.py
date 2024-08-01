from loader import bot
from telebot.types import Message
from api.core import get_request
from database.common.models import Password
from api.core import logger
from keyboards.reply.start_reply import gen_markup


@bot.message_handler(func=lambda message: message.text == 'Генерация пароля 🔑')
def gen_password(message):
    try:
        password_str = get_request(12)
        # Сохраняем сгенерированный пароль в базу данных
        new_password = Password.create(password=password_str, user_id=message.chat.id)
        new_password.save()
        bot.reply_to(message, f'Ваш случайный пароль: {password_str}', reply_markup=gen_markup())
    except Exception as e:
        logger.error(f'Ошибка: {str(e)}')
        bot.reply_to(message, f'Ошибка: {str(e)}')


@bot.message_handler(commands=['generate'])
def generate(message: Message) -> None:
    try:
        # Получаем длину пароля из аргументов команды
        length = int(message.text.split()[1])
        if length < 12:
            bot.reply_to(message, 'Пароль должен быть не менее 12 символов.')
        else:
            password_str = get_request(length)
            # Сохраняем сгенерированный пароль в базу данных
            new_password = Password.create(password=password_str, user_id=message.chat.id)
            new_password.save()
            bot.reply_to(message, f'Ваш случайный пароль: {password_str}', reply_markup=gen_markup())
    except IndexError:
        bot.reply_to(message, 'Пожалуйста, укажите длину пароля. Используйте команду /generate <длина>.')
    except ValueError:
        bot.reply_to(message, 'Длина пароля должна быть целым числом.')
    except Exception as e:
        logger.error(f'Ошибка: {str(e)}')
        bot.reply_to(message, f'Ошибка: {str(e)}')
