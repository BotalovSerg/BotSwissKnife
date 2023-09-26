from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import CMD_LEXICON_RU

router: Router = Router()


@router.message(CommandStart())
async def cd_start(message: Message):
    await message.answer(text=CMD_LEXICON_RU['/start'])


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(text=CMD_LEXICON_RU['/help'])


@router.message(Command("support"))
async def cmd_help(message: Message):
    await message.answer(text=CMD_LEXICON_RU['/support'])
