import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from handlers import user_handlers, weather_handlers
from keyboards.set_menu import set_main_menu


async def main_bot() -> None:

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(weather_handlers.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main_bot())
