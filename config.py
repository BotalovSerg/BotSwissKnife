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


def load_config(path: str | None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
