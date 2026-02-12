import asyncio
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


async def main():
   await dp.start_polling(bot)   

asyncio.run(main())