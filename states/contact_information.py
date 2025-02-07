from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    """ Функция наименования состояний """

    location = State()
    name = State()
    age = State()
    country = State()
    city = State()
    phone_number = State()
