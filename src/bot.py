"""Сервер Telegram бота, запускаемый непосредственно"""
import os
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, CallbackQuery
from aiogram.utils.markdown import text, bold

from cropped_img import cropped_img
from my_logging import logger
from parser import pars_img
from keyboard import choice, profile_keyboard

API_TOKEN = os.getenv("NOMAD_BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


"""Обработчик команд"""


@logger.catch
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message) -> None:
    """Отправляет приветственное сообщение и помощь по боту"""
    first_msg = text(bold("Привет, меня зовут Васянчик🧠. \n "
                          "Я могу скинуть тебе расписание шараги"))
    await message.answer(first_msg, parse_mode=ParseMode.MARKDOWN,
                         reply_markup=choice)


@logger.catch
@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    """Отсылает фото расписания"""
    try:

        time.sleep(1)
        pars_img()
        cropped_img()
        with open('schedule/schedule2.png', 'rb') as f:
            if not os.path.isdir('schedule'):
                os.mkdir('schedule')
            if os.path.isfile('schedule/schedule2.png'):
                os.remove('schedule/schedule2.png')
                os.remove('schedule/schedule.png')
                logger.info("Удалил расписание")
            contents = f.read()
            await bot.send_photo(message.from_user.id, photo=contents)
            logger.info("Расписание успешно отправлено")
    except Exception:
        logger.error("no png file")
        msg_error = "Упс.. У меня нет расписания 😱 \n" \
                    "Напиши: /download и я скачаю его 💾\n" \
                    "Или нажми на кнопку - Скачать расписание 🕹"
        await message.answer(msg_error, parse_mode=ParseMode.MARKDOWN)


"""Обработчик кнопок"""


# кнопки по профилю
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


# -----------------------------------------------------

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
@dp.callback_query_handler(text="schedule")
async def schedule_buying(call: CallbackQuery):
    try:
        time.sleep(2)
        pars_img()
        cropped_img()
        with open('schedule/schedule2.png', 'rb') as f:
            if not os.path.isdir('schedule'):
                os.mkdir('schedule')
            if os.path.isfile('schedule/schedule2.png'):
                os.remove('schedule/schedule2.png')
                os.remove('schedule/schedule.png')
                logger.info("Удалил расписание")
            contents = f.read()
            await bot.send_photo(call.from_user.id, photo=contents)
            logger.info("Расписание успешно отправлено")
    except Exception:
        logger.error("no png file")
        msg_error = "Упс.. У меня нет расписания 😱"
        await call.answer(msg_error, show_alert=True)


@logger.catch
@dp.callback_query_handler(text="profile")
async def profile_user(call: CallbackQuery):
    """Открывает клавиатуру для показа профиля пользователя"""
    await call.message.edit_reply_markup(reply_markup=profile_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
