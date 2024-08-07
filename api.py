import requests
import datetime
from datetime import date

current_date = date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()


def weather_by_city(city_name):
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': '1e939dbf9086b6944ab2afc6354f4fa1',
        'units': 'metric',
        'lang': 'ru'
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    return weather

# w = weather_by_city(input('Введите название города: '))
# print(f'Температура в {w['name']}: {w["main"]["temp"]}°C')
# print(f'Описание погоды: {w["weather"][0]["description"]}')
# print(f'Влажность: {w["main"]["humidity"]}%')
# print(f'Давление: {w["main"]["pressure"]} мм рт.ст.')
# print(f'Скорость ветра: {w["wind"]["speed"]} м/с')
# print(f'Направление ветра: {w["wind"]["deg"]}°')
# print(f'Дата и время получения данных: {current_date}, {current_time.replace(microsecond=0)}')