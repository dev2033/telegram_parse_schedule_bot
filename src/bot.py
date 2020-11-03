"""Сервер Telegram бота, запускаемый непосредственно"""
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, bold, italic, code

from my_logging import logger
from parser import pars_img
from messages import (
    download_sch_msg_1,
    download_sch_msg_2,
    schedule_img_msg_1,
    schedule_img_msg_2
)

API_TOKEN = os.getenv("NOMAD_BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@logger.catch
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    first_msg = text(bold("Привет, меня зовут Васянчик, "
                          "напиши /help чтобы узнать что я могу"))

    await message.answer(first_msg, parse_mode=ParseMode.MARKDOWN)


@logger.catch
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """Отправляет руководство по боту"""

    msg = f"{download_sch_msg_1} - {download_sch_msg_2} \n\n" \
          f"{schedule_img_msg_1} - {schedule_img_msg_2}"

    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@logger.catch
@dp.message_handler(commands=['download'])
async def pars_site(message: types.Message):
    pars_img()
    msg = "Расписание успешно скачано 👌 \n" \
          "Напиши /photo и я перешлю тебе его 📲"
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@logger.catch
@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    """Отсылает фото расписания"""
    try:
        with open('schedule/schedule.png', 'rb') as f:
            contents = f.read()
    except FileNotFoundError:
        logger.error("no png file")
        msg_error = "Упс.. У меня нет расписания 😱 \n" \
                    "Напиши: /download и я скачаю его 💾"
        await message.answer(msg_error, parse_mode=ParseMode.MARKDOWN)

    msg = "A вот и расписание👆\nСмотри мне! НЕ ПРОГУЛИВАЙ 🤡"

    await bot.send_photo(message.from_user.id, photo=contents)
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
