"""Кнопки для бота"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Главная клавиатура
choice = InlineKeyboardMarkup()

update_schedule_btn = InlineKeyboardButton(text='Удалить старое расписание',
                                           callback_data='update')
download_btn = InlineKeyboardButton(text='Скачать расписание',
                                    callback_data='download')
schedule_btn = InlineKeyboardButton(text='Прислать расписание',
                                    callback_data='schedule')
cancel_btn = InlineKeyboardButton(text='Закрыть', callback_data='cancel')
help_btn = InlineKeyboardButton(text='Помощь', callback_data='help')
developer_btn = InlineKeyboardButton(text='Разработчик',
                                     callback_data='dev')

profile = InlineKeyboardButton(text='Мой профиль', callback_data='profile')

choice.add(update_schedule_btn)
choice.add(download_btn)
choice.add(schedule_btn)
choice.add(help_btn, profile)
choice.add(developer_btn)
choice.add(cancel_btn)


# Клавиатура для показа профиля пользователя
profile_keyboard = InlineKeyboardMarkup()

my_id = InlineKeyboardButton(text='Мой ID', callback_data='my_id')
my_username = InlineKeyboardButton(text='Мой username',
                                   callback_data='my_username')
my_first_name = InlineKeyboardButton(text='Мое имя', callback_data='first_name')
my_last_name = InlineKeyboardButton(text='Моя фамилия',
                                    callback_data='last_name')
home = InlineKeyboardButton(text='Главная', callback_data='home')

profile_keyboard.add(my_id)
profile_keyboard.add(my_username)
profile_keyboard.add(my_first_name)
profile_keyboard.add(my_last_name)
profile_keyboard.add(home)
