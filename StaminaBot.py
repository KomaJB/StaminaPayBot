import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


# ===== TOKEN из Render =====
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing in environment variables")


# ===== Bot setup =====
bot = Bot(token=TOKEN)
dp = Dispatcher()


# ===== /start handler =====
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Бот запущен и работает ✅")


# ===== main loop =====
async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())