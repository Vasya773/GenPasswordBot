from loader import bot
from keyboards.reply.contact import request_contact
from telebot.types import Message
from states.contact_information import UserInfoState
from keyboards.reply.start_reply import gen_markup


@bot.message_handler(commands=['survey'])
def start_survey(message: Message) -> None:
    """ Функция начала опроса (получение имени пользователя) """

    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name}. Введи своё имя\n'
                                           f'Нажми /cancel если хочешь закончить')


@bot.message_handler(func=lambda message: message.text == 'Опрос 📝')
def start_survey(message: Message) -> None:
    """ Функция начала опроса (получение имени пользователя) """

    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name}. Введи своё имя\n'
                                           f'Нажми /cancel если хочешь закончить')


@bot.message_handler(state='*', commands=['cancel'])
def any_state(message):
    """ Функция конца опроса """

    bot.send_message(message.chat.id, f'Опрос окончен.\n', reply_markup=gen_markup())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    """ Функция получения возраста от пользователя """

    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Спасибо записал. Теперь введи свой возраст')
        bot.set_state(message.from_user.id, UserInfoState.age, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text

    else:
        bot.send_message(message.from_user.id, 'Имя может содержать только буквы'
                                               'Попробуй ещё раз')


@bot.message_handler(state=UserInfoState.age)
def get_age(message: Message) -> None:
    """ Функция получения страны от пользователя """

    if message.text.isdigit():
        bot.send_message(message.from_user.id, 'Спасибо записал. Теперь введи свою страну проживания')
        bot.set_state(message.from_user.id, UserInfoState.country, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['age'] = message.text

    else:
        bot.send_message(message.from_user.id, 'Возраст может быть только числом\n'
                                               'Попробуй ещё раз')


@bot.message_handler(state=UserInfoState.country)
def get_country(message: Message) -> None:
    """ Функция получения города от пользователя """

    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Спасибо записал. Теперь введи свой город')
        bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['country'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Страна может содержать только буквы\n'
                                               'Попробуй ещё раз')


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    """ Функция получения номера телефона от пользователя """

    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Спасибо записал. Отправь свой номер, нажав на кнопку',
                         reply_markup=request_contact())
        bot.set_state(message.from_user.id, UserInfoState.phone_number, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Город может содержать только буквы\n'
                                               'Попробуй ещё раз')


@bot.message_handler(content_types=['text', 'contact'], state=UserInfoState.phone_number)
def get_contact(message: Message) -> None:
    """ Функция получения информации на основе проведённого опроса для пользователя """

    if message.content_type == 'contact':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['phone_number'] = message.contact.phone_number

        text = (f'Спасибо за предоставленную информацию. Ваши данные:\n'
                f'Имя - {data['name']}\nВозраст - {data['age']}\nСтрана - {data['country']}\n'
                f'Город - {data['city']}\nНомер телефона - {data['phone_number']}\n')
        bot.send_message(message.from_user.id, text, reply_markup=gen_markup())
    else:
        bot.send_message(message.from_user.id, 'Чтобы отправить контактную информацию нажми на кнопку\n'
                                               'Попробуй ещё раз')
