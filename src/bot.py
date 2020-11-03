"""Сервер Telegram бота, запускаемый непосредственно"""
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, bold, italic, code

from my_logging import logger
from parser import pars_img

API_TOKEN = os.getenv("NOMAD_BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    first_msg = text(bold("Бот для учёта финансов"))
    today_msg = text(code("Сегодняшняя статистика:"), bold("/today"))
    month_msg = text(code("За текущий месяц:"), bold("/month"))
    expenses_msg = text(code("Последнии внесённые расходы:"), bold("/expenses"))
    categories_msg = text(code("Категории трат:"), bold("/categories"))
    add_finance_msg = text(bold("Чтобы добавить расход:"), italic("250 такси"))

    msg = f"{first_msg}\n\n{today_msg}\n" \
          f"{month_msg}\n" \
          f"{expenses_msg}\n" \
          f"{categories_msg}\n\n" \
          f"{add_finance_msg}"

    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['parser'])
async def pars_site(message: types.Message):
    pars_img()
    msg = "Картинка успешно скачана" \
          "Напиши /photo и я тебе скину его))"
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    with open('schedule/schedule.png', 'rb') as f:
        contents = f.read()
    await bot.send_photo(message.from_user.id, photo=contents)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)