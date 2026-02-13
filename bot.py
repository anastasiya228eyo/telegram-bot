import asyncio
import python_weather

WEATHER_TRANSLATE = {
    "clear": "ясно",
    "sunny": "солнечно",
    "partly cloudy": "переменная облачность",
    "cloudy": "облачно",
    "overcast": "пасмурно",
    "mist": "туман",
    "fog": "туман",
    "light rain": "небольшой дождь",
    "rain": "дождь",
    "heavy rain": "сильный дождь",
    "snow": "снег",
    "light snow": "небольшой снег",
    "heavy snow": "сильный снег",
    "thunderstorm": "гроза"
}

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8395368621:AAGxPPU6pYFnmq5AK7ovdIsJmXkgBpdIn8I"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("ещкере")

@dp.message()
async def chat(message: types.Message):
    if not message.text:
        return

    text = message.text.lower()

    if "спасибо" in text:
        await message.reply("в кармашек не положишь")

    if "привет" in text:
        await message.reply("ещкере")

    if text == "да":
        await message.reply("пизда")

    if message.text.lower().startswith("погода "):
        city = message.text[7:].strip()

    try:
        async with python_weather.Client() as client:
            weather = await client.get(city)

        temp = weather.temperature
        desc = weather.description.lower()
        desc = WEATHER_TRANSLATE.get(desc, desc)

        await message.reply(f"Сейчас в городе {city.title()} {desc}, {temp}°C")

    except Exception:
        await message.reply("Не смог найти такой город")


async def main():
   await dp.start_polling(bot)   

asyncio.run(main())