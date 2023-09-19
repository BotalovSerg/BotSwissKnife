from typing import TypeAlias
from dataclasses import dataclass
from environs import Env
from .coordinates import Coordinates
from urllib.request import urlopen
import json


Celsius: TypeAlias = float


@dataclass
class WeatherApiKey:
    api_key: str


def load_api_key_weather(path: str | None = None):
    env = Env()
    env.read_env(path)

    return WeatherApiKey(api_key=env('WEATHER_API_KEY'))


@dataclass(slots=True, frozen=True)
class GetWeather:
    location: str
    temperature: Celsius
    temperature_feeling: Celsius
    description: str


def _get_openweather_response(latitude: float, longitude: float, api_key) -> str:
    get_api = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    return urlopen(get_api).read()


def get_weather(coordinates=Coordinates) -> GetWeather:
    api_key = load_api_key_weather().api_key
    response = _get_openweather_response(
        coordinates.latitude, coordinates.longitude, api_key)
    weather = _parse_pesponse(response)
    return weather


def _parse_pesponse(response: str) -> GetWeather:
    dict_response = json.loads(response)
    temp = dict_response['main']['temp']
    location = dict_response['name']
    temperature_feeling = dict_response['main']['feels_like']
    description = str(dict_response['weather'][0]['description'])

    # print(temp)
    # print(location)
    return GetWeather(
        location=location,
        temperature=temp,
        temperature_feeling=temperature_feeling,
        description=description
    )


# get_weather(get_cor)
# print(_get_openweather_response(
#     get_cor.latitude, get_cor.longitude, api_key.api_key))


# b'{"coord":{"lon":60.6083,"lat":56.8456},
# "weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
# "base":"stations","main":{"temp":20.83,"feels_like":20.09,"temp_min":20.45,"temp_max":20.83,
#                           "pressure":1023,"humidity":43},"visibility":10000,"wind":
# {"speed":4,"deg":300},"clouds":{"all":0},"dt":1694684345,"sys":
# {"type":1,"id":8985,"country":"RU","sunrise":1694654717,"sunset":1694701302},
# "timezone":18000,"id":1486209,"name":"Ekaterinburg","cod":200}'

# {'coord': {'lon': 60.6122, 'lat': 56.8519},
#  'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
#  'base': 'stations',
#  'main': {'temp': 20.81, 'feels_like': 20.07, 'temp_min': 20.43, 'temp_max': 20.81, 'pressure': 1022, 'humidity': 43},
#  'visibility': 10000,
#  'wind': {
#     'speed': 3, 'deg': 340},
#     'clouds': {'all': 0},
#     'dt': 1694684853,
#     'sys': {'type': 1, 'id': 8985, 'country': 'RU', 'sunrise': 1694654716, 'sunset': 1694701301},
#     'timezone': 18000, 'id': 1486209, 'name': 'Ekaterinburg', 'cod': 200}
