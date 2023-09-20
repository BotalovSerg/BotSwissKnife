from datetime import datetime
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
    sunrise: datetime
    sunset: datetime


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
    sunrise = datetime.fromtimestamp(dict_response['sys']['sunrise'])
    sunset = datetime.fromtimestamp(dict_response['sys']['sunset'])

    return GetWeather(
        location=location,
        temperature=temp,
        temperature_feeling=temperature_feeling,
        description=description,
        sunrise=sunrise,
        sunset=sunset
    )
