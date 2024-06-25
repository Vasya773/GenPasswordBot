from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from database.common.models import db, History


@bot.message_handler(commands=['city_user'])
def city_weather(message: Message):
    """ Функция получения города от пользователя для определения погодных условий """

    bot.set_state(message.from_user.id, UserInfoState.location, message.chat.id)

    response = 'Введите город: '
    bot.send_message(message.from_user.id, response)

    with db:
        History.create(user_id=message.from_user.id, first_name=message.from_user.first_name,
                       response=response)


@bot.message_handler(state=UserInfoState.location)
def get_location(message: Message) -> None:
    if message.text.isalpha():
        response = 'Спасибо, записал.'
        bot.send_message(message.from_user.id, response)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['location'] = message.text

    else:
        response = 'Город может содержать только буквы'
        bot.send_message(message.from_user.id, response)

    # with db:
    #     History.create(user_id=message.from_user.id, first_name=message.from_user.first_name,
    #                    response=response)
