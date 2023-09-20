from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_WEATHER_KB


def create_inline_kb(**kwargs) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for text_btn, data in kwargs.items():
        buttons.append(InlineKeyboardButton(
            text=text_btn,
            callback_data=data
        ))

    kb_builder.row(*buttons)

    return kb_builder.as_markup()
