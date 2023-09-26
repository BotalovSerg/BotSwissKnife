from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU, LEXICON_WEATHER_KB
from keyboards.inline_weather_kb import create_inline_kb

router: Router = Router()


@router.message(CommandStart())
async def cd_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command("support"))
async def cmd_help(message: Message):
    await message.answer(text=LEXICON_RU['/support'])


@router.message(Command("id_user"))
async def cmd_user_id(message: Message):
    await message.answer(text=f"Your ID: {message.from_user.id}")


# @router.message(Command("test"))
# async def cmd_test(message: Message):
#     kb = create_inline_kb(**LEXICON_WEATHER_KB)
#     await message.answer(
#         text='Test kb weather',
#         reply_markup=kb
#     )
