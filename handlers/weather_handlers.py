from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from weathear.api_service import get_weather
from weathear.coordinates import get_coordinates

router: Router = Router()


@router.message(Command("weather"))
async def cmd_weather(message: Message):
    answ = get_weather(get_coordinates())

    await message.answer(f"City: {answ.location}, {answ.description} \
                         \nTemperature is: {answ.temperature}°C, \
                         feels like {answ.temperature_feeling}°C")
