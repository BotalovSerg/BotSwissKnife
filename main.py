from config import load_config


conf = load_config('./.env')
token = conf.tg_bot.token
