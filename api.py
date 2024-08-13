import requests
import datetime
from datetime import date

current_date = date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()


def weather_by_city(city_name: str) -> dict:
    """
    Подключаемся к api.

    Получаем различные парамется погодных условий.

    Args:
        city_name: str (Название города)

    Returns:
        dict: Возвращаем результат функции в виде словаря погодных условий
    """
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
