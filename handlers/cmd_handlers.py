import json
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import CMD_LEXICON_RU

router: Router = Router()


@router.message(CommandStart())
async def cd_start(message: Message):
    with open("/home/sb/BotSwissKnife/users/users.json", "r") as f_o:
        data_from_json = json.load(f_o)
    user_id = message.from_user.id
    username = message.from_user.username

    if str(user_id) not in data_from_json:
        data_from_json[user_id] = {"username": username}
    
    with open("/home/sb/BotSwissKnife/users/users.json", "w") as f_o:
        json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)

    await message.answer(text=CMD_LEXICON_RU['/start'])
    await message.answer(text=f"You are registered with BotSwissKnife\n"
                         f"Your id : {user_id},\nName : {username}")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(text=CMD_LEXICON_RU['/help'])


@router.message(Command("support"))
async def cmd_help(message: Message):
    await message.answer(text=CMD_LEXICON_RU['/support'])
