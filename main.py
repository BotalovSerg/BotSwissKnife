import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config_data.config import load_config, Config
from handlers import user_handlers


async def main_bot() -> None:

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.startup.register(set_main_menu)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def set_main_menu(bot: Bot):

    main_menu_commands = [
        BotCommand(command='/help',
                   description='Спарвка по работе бота')
    ]
    await bot.set_my_commands(main_menu_commands)

if __name__ == '__main__':
    asyncio.run(main_bot())
