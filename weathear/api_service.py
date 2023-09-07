from dataclasses import dataclass
from environs import Env
from coordinates import get_coordinates
from urllib.request import urlopen
import json


@dataclass
class Weather:
    api_key: str


def load_api_key_weather(path: str | None = None):
    env = Env()
    env.read_env(path)

    return Weather(api_key=env('WEATHER_API_KEY'))


get_cor = get_coordinates()
api_key = load_api_key_weather()


# get_api = f'https://api.openweathermap.org/data/2.5/weather?lat={get_cor.latitude}&lon={get_cor.longitude}&appid={api_key.api_key}&units=metric'


def _get_openweather_response(latitude: float, longitude: float, api_key) -> str:
    get_api = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    return urlopen(get_api).read()


print(_get_openweather_response(
    get_cor.latitude, get_cor.longitude, api_key.api_key))
