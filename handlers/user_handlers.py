from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import KEYBOARD_MENU
from keyboards.inline_create_kb import create_inline_kb

router: Router = Router()


@router.message(Command("test"))
async def cmd_test(message: Message):
    kb = create_inline_kb(2, **KEYBOARD_MENU)
    await message.answer(
        text="📍 Main menu",
        reply_markup=kb
    )


@router.callback_query(F.data == "id_user")
async def cmd_user_id(callback: CallbackQuery):
    await callback.message.edit_text(f"Your ID: {callback.message.from_user.id}")
    await callback.answer()
