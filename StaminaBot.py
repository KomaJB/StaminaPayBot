import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers.start import start_handler
from aiogram.filters import Command

bot = Bot(token=TOKEN)
dp = Dispatcher()

# регистрируем хендлер
dp.message.register(start_handler, Command("start"))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())