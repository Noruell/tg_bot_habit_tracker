import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ========== НАСТРОЙКИ ==========
BOT_TOKEN = "8762811320:AAEMIQ0yGhPUj4MoCJA7nKDEjDTMDh8TMqE"
# =================================

bot = Bot(token=BOT_TOKEN)
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

@dp.message(Command("add"))
async def cmd_add(message: types.Message):
    await message.answer(
        "Добавил привычку"
    )


# ========== ЗАПУСК ==========
async def main():
    logging.basicConfig(level=logging.INFO)
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())