"""Сервер Telegram бота, запускаемый непосредственно"""
import glob
import os
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, CallbackQuery
from aiogram.utils.markdown import text, bold

from cropped_img import cropped_img
from my_logging import logger
from parser import pars_img
from messages import (
    download_sch_msg_1, download_sch_msg_2,
    schedule_img_msg_1, schedule_img_msg_2,
    start_msg_1, start_msg_2,
    info_developer_msg_1, info_developer_msg_2
)
from keyboard import choice, profile_keyboard


API_TOKEN = os.getenv("NOMAD_BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@logger.catch
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message) -> None:
    """Отправляет приветственное сообщение и помощь по боту"""
    first_msg = text(bold("Привет, меня зовут Васянчик🧠, "
                          "напиши /help чтобы узнать что я могу \n"
                          "Или воспользуйся кнопками ниже"))
    await message.answer(first_msg, parse_mode=ParseMode.MARKDOWN,
                         reply_markup=choice)


@logger.catch
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """Отправляет руководство по боту"""
    msg = f"{download_sch_msg_1} - {download_sch_msg_2} \n\n" \
          f"{schedule_img_msg_1} - {schedule_img_msg_2} \n\n" \
          f"{start_msg_1} - {start_msg_2} \n\n" \
          f"Или воспользуйся клавиатурой ниже ⌨️"

    await message.answer(msg, parse_mode=ParseMode.MARKDOWN,
                         reply_markup=choice)


@logger.catch
@dp.message_handler(commands=['download'])
async def parse_site(message: types.Message):
    """
    Обработка команды /download
    Вызывает функцию pars_img, которая качает
    фото с сайта и сохраняет в папке schedule
    """
    pars_img()
    cropped_img()
    msg = "Расписание успешно скачано 👌 \n" \
          "Напиши /photo и я перешлю тебе его 📲"
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN,
                         reply_markup=choice)


@logger.catch
@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    """Отсылает фото расписания"""
    try:
        with open('schedule/schedule2.png', 'rb') as f:
            contents = f.read()
    except FileNotFoundError:
        logger.error("no png file")
        msg_error = "Упс.. У меня нет расписания 😱 \n" \
                    "Напиши: /download и я скачаю его 💾\n" \
                    "Или нажми на кнопку - Скачать расписание 🕹"
        await message.answer(msg_error, parse_mode=ParseMode.MARKDOWN)

    msg = "A вот и расписание👆\nСмотри мне! НЕ ПРОГУЛИВАЙ 🤡"
    await bot.send_photo(message.from_user.id, photo=contents)
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)
    logger.info("Расписание успешно отправлено")


# Обработчик кнопок

@logger.catch
@dp.callback_query_handler(text="my_id")
async def user_id(call: CallbackQuery):
    msg_user = call.from_user.id
    msg = f"Ваш ID:\n {msg_user}"
    await call.answer(msg, show_alert=True)


@logger.catch
@dp.callback_query_handler(text="my_username")
async def user_username(call: CallbackQuery):
    msg_user = call.from_user.username
    msg = f"Ваш username:\n {msg_user}"
    await call.answer(msg, show_alert=True)


@logger.catch
@dp.callback_query_handler(text="first_name")
async def user_firstname(call: CallbackQuery):
    msg_user = call.from_user.first_name
    msg = f"Ваше имя:\n {msg_user}"
    await call.answer(msg, show_alert=True)


@logger.catch
@dp.callback_query_handler(text="last_name")
async def user_lastname(call: CallbackQuery):
    msg_user = call.from_user.last_name
    msg = f"Ваша фамилия:\n {msg_user}"
    await call.answer(msg, show_alert=True)


@logger.catch
@dp.callback_query_handler(text="home")
async def home_keyboard(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=choice)


@logger.catch
@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    """
    Обрабатывает callback = cancel -
    Закрывает инлайн клавиатуру
    """
    await call.answer("Вы закрыли клавиатуру", show_alert=False)
    await call.message.edit_reply_markup(reply_markup=None)


@logger.catch
@dp.callback_query_handler(text="download")
async def download_buying(call: CallbackQuery):
    """
    Обрабатывает кнопку с callback = download
    Парсит и скачивает фото с расписанием
    """
    try:
        pars_img()
        time.sleep(3)
        cropped_img()
        time.sleep(3)
    except Exception:
        logger.exception("no download schedule")
        await call.answer("Не удалось скачать расписание! Повтори позже :(")
    await call.answer("Расписание скачано! 📩")


@logger.catch
@dp.callback_query_handler(text="remove")
async def update_schedule(call: CallbackQuery):
    """Удаляет расписание"""
    upd_schedule = glob.glob('schedule/*.png')
    for file in upd_schedule:
        try:
            os.remove(file)
            logger.info("Расписание удалено")
        except OSError:
            await call.answer("Не удалось удалить расписание", show_alert=True)
            logger.exception("not remove schedule")
        await call.answer("Расписание удалено", show_alert=True)


@logger.catch
@dp.callback_query_handler(text="schedule")
async def schedule_buying(call: CallbackQuery):
    try:
        with open('schedule/schedule2.png', 'rb') as f:
            contents = f.read()
    except FileNotFoundError:
        logger.error("no png file")
        msg_error = "Упс.. У меня нет расписания 😱 \n" \
                    "Напиши: /download и я скачаю его 💾\n" \
                    "Или воспользуйся клавиатурой ниже⌨️\n\n" \
                    "* Если клавиатуры нет, напиши /start "
        await call.answer(msg_error, show_alert=True)

    msg = "А вот и расписание 🤡"
    await bot.send_photo(call.from_user.id, photo=contents)
    await call.answer(msg, show_alert=False)


@logger.catch
@dp.callback_query_handler(text="dev")
async def developer_info(call: CallbackQuery):
    """
    Обрабатывает кнопку с callback = instruction
    Показывает информацию о разработчике
    """
    msg = f"{info_developer_msg_1}: \n\n{info_developer_msg_2}"
    await call.answer(msg, show_alert=True)


@logger.catch
@dp.callback_query_handler(text="profile")
async def profile_user(call: CallbackQuery):
    """Открывает клавиатуру для показа профиля пользователя"""
    await call.message.edit_reply_markup(reply_markup=profile_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
