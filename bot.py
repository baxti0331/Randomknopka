from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Получим токен из переменной окружения
WEB_APP_URL = https://random-wine.vercel.app/

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="PLAY 🕹️", web_app=WebAppInfo(url=WEB_APP_URL))]
        ]
    )
    await message.answer("Нажмите кнопку ниже, чтобы запустить мини-приложение 🎲", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
