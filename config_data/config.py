from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str
    # admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    # db: DatabaseConfig


def load_config(path: str | None = None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


# @dataclass
# class Weather:
#     api_key: str


# def load_api_key_weather(path: str | None = None):
#     env = Env()
#     env.read_env(path)

#     return Weather(api_key=env('WEATHER_API_KEY'))
