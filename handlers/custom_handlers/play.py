from loader import bot
from database.common.models import Game
import random
from keyboards.reply.start_reply import gen_markup
from telebot.types import ReplyKeyboardRemove


@bot.message_handler(func=lambda message: message.text == 'Угадай число 🎮')
def guess_number(message) -> None:
    """Начинает игру 'Угадай число'."""

    number_to_guess = random.randint(1, 100)  # Генерируем число от 1 до 100
    Game.create(user_id=message.chat.id, number=number_to_guess, attempts=0)
    bot.reply_to(message, "Игра началась! Я загадал число от 1 до 100.\nПопробуйте угадать его!\n\n"
                          "Чтобы закончить игру введите '0'", reply_markup=ReplyKeyboardRemove())


@bot.message_handler(commands=['play'])
def guess_number(message) -> None:
    """Начинает игру 'Угадай число'."""

    number_to_guess = random.randint(1, 100)  # Генерируем число от 1 до 100
    Game.create(user_id=message.chat.id, number=number_to_guess, attempts=0)
    bot.reply_to(message, "Игра началась! Я загадал число от 1 до 100.\nПопробуйте угадать его!\n\n"
                          "Чтобы закончить игру введите '0'", reply_markup=ReplyKeyboardRemove())


# Обработчик сообщений для игры
@bot.message_handler(func=lambda message: Game.select().where(Game.user_id == message.chat.id).exists(),
                     content_types=['text'])
def check_number(message) -> None:
    """Обрабатывает попытки угадывания числа."""

    try:
        guess = int(message.text)
        game = Game.get(Game.user_id == message.chat.id)

        if guess == 0:
            bot.reply_to(message, f"Игра окончена.\n"
                                  f"Количество попыток: {game.attempts}", reply_markup=gen_markup())
            game.delete_instance()  # Удаляем запись после завершения игры
            return

        elif guess < 1 or guess > 100:
            bot.reply_to(message, "Число должно быть от 1 до 100. Попробуйте снова.")
            return

        game.attempts += 1
        game.save()

        if guess < game.number:
            bot.reply_to(message, "Мое число больше. Попробуйте еще раз.")
        elif guess > game.number:
            bot.reply_to(message, "Мое число меньше. Попробуйте еще раз.")
        else:
            bot.reply_to(message, f"Поздравляю! Вы угадали число {game.number} за {game.attempts} попыток.",
                         reply_markup=gen_markup())
            game.delete_instance()
            return

    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число от 1 до 100.")
