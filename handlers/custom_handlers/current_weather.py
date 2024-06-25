from loader import bot
from config_data.config import api_key
from telebot.types import Message
from api.utils.site_api_handler import get_weather
from database.common.models import db, History


@bot.message_handler(commands=['current_weather'])
def get_weather(message: Message):
    """ Функция получения погодных условий на основе отправленного пользователем города """

    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            location = data['location']

            response = get_weather(method_endswith='weather',
                                   params={'q': location, 'appid': api_key, 'units': 'metric', 'lang': 'ru'},
                                   method_type='GET'
                                   )
            print(data)

        bot.send_message(message.from_user.id, response)

    # code_to_smile = {
    #     "Clear": "Ясно \U00002600",
    #     "Clouds": "Облачно \U00002601",
    #     "Rain": "Дождь \U00002614",
    #     "Drizzle": "Дождь \U00002614",
    #     "Thunderstorm": "Гроза \U000026A1",
    #     "Snow": "Снег \U0001F328",
    #     "Mist": "Туман \U0001F32B"
    # }
    #
    # try:
    #     response = requests.get(
    #         f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'
    #     )
    #     data = response.json()
    #
    #     city = data['name']
    #     cur_weather = data['main']['temp']
    #
    #     weather_description = data['weather'][0]['main']
    #     if weather_description in code_to_smile:
    #         wd = code_to_smile[weather_description]
    #     else:
    #         wd = 'Посмотри в окно, не пойму что там за погода!'
    #
    #     humidity = data['main']['humidity']
    #     pressure = data['main']['pressure']
    #     wind = data['wind']['speed']
    #     sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    #     sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    #     length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
    #         data['sys']['sunrise'])
    #
    #     print(f'***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n'
    #           f'Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n'
    #           f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n'
    #           f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n'
    #           f'Продолжительность дня: {length_of_the_day}\n'
    #           f'Хорошего дня!'
    #           )

    except Exception as exc:
        print(exc)
        response = 'Выберете город и попробуйте снова'
        bot.send_message(message.from_user.id, response)

    # with db:
    #     History.create(user_id=message.from_user.id, first_name=message.from_user.first_name,
    #                    response=response)
