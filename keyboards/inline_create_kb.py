from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_inline_kb(width, **kwargs) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for text_btn, data in kwargs.items():
        buttons.append(InlineKeyboardButton(
            text=text_btn,
            callback_data=data
        ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()
