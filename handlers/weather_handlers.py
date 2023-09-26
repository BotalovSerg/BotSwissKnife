from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.filters import Command
from weathear.api_service import get_weather
from weathear.coordinates import get_coordinates
from lexicon.lexicon import LEXICON_WEATHER_KB
from keyboards.inline_create_kb import create_inline_kb


router: Router = Router()


@router.callback_query(F.data == "weather")
async def press_btn_weather(callback: CallbackQuery):
    answ = get_weather(get_coordinates())
    text = f"City: {answ.location}, {answ.description} \
                         \nTemperature is: {answ.temperature}°C, \
                         feels like {answ.temperature_feeling}°C"
    await callback.message.edit_text(
        text=text,
        reply_markup=callback.message.reply_markup
    )
    await callback.answer()


@router.callback_query(F.data == "sun")
async def press_btn_sun(callback: CallbackQuery):
    answ = get_weather(get_coordinates())
    text = f"Sunrise: {answ.sunrise.strftime('%H:%M')} \
             \nSunset: {answ.sunset.strftime('%H:%M')}"

    await callback.message.edit_text(
        text=text,
        reply_markup=callback.message.reply_markup
    )
    await callback.answer()


@router.message(Command("weather"))
async def cmd_weather(message: Message):
    kb = create_inline_kb(2, **LEXICON_WEATHER_KB)
    await message.answer(
        text='Press the weather or sun button',
        reply_markup=kb
    )
