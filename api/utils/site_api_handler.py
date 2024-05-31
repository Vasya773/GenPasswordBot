import requests
import datetime
from loader import bot
from config_data.config import SiteSettings
from telebot.types import Message


@bot.message_handler()
def _get_weather(message: Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={site.api_key}&units=metric'
        )
        data = response.json()

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description == code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не пойму что там за погода!'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise']
        )

        bot.reply_to(f'***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n'
                     f'Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n'
                     f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n'
                     f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n'
                     f'Продолжительность дня: {length_of_the_day}\n'
                     f'***Хорошего дня!***'
                     )
    except:
        bot.reply_to('\U00002620 Проверьте название города \U00002620')


class SiteApiInterface():

    @staticmethod
    def get_weather():
        return _get_weather


site = SiteSettings()
if __name__ == '__main__':
    _get_weather()

    SiteApiInterface()
