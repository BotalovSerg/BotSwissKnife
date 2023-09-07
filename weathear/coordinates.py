from dataclasses import dataclass
from urllib.request import urlopen
import json


@dataclass
class Coordinates:
    latitude: float
    longitude: float


def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)


def get_coordinates() -> Coordinates:
    data = _get_ip_data()
    latitude = data['loc'].split(',')[0]
    longitude = data['loc'].split(',')[1]

    return Coordinates(latitude=latitude, longitude=longitude)
