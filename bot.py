import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ========== НАСТРОЙКИ ==========
# 👇 ВСТАВЬ СВОЙ ТОКЕН (получи у @BotFather)
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
PROXY_URL = "http://206.123.156.230:8517"


# Включаем логирование (чтобы видеть ошибки)
logging.basicConfig(level=logging.INFO)

# Создаём объекты
bot = Bot(token=BOT_TOKEN, proxy=PROXY_URL)
dp = Dispatcher()


# ========== КОМАНДЫ ==========
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот-трекер привычек.\n\n"
        "Вот что я умею:\n"
        "/add — добавить привычку\n"
        "/list — показать все привычки\n"
        "/check — отметить выполнение\n\n"
        "Скоро добавлю базу данных и кнопки! 🚀"
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📋 Доступные команды:\n"
        "/start — приветствие\n"
        "/help — эта подсказка\n"
        "/add — добавить привычку\n"
        "/list — список привычек\n"
        "/check — отметить выполнение"
    )


# ========== ЗАПУСК ==========
async def main():
    print("✅ Бот запущен и работает...")
    await dp.start_polling(bot, polling_timeout=15)

if __name__ == "__main__":
    asyncio.run(main())