from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(CommandStart())
async def cd_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])
