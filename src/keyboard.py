"""Кнопки для бота"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


choice = InlineKeyboardMarkup()

download_btn = InlineKeyboardButton(text='Скачать расписание',
                                    callback_data='download')
schedule_btn = InlineKeyboardButton(text='Прислать расписание',
                                    callback_data='schedule')
cancel_btn = InlineKeyboardButton(text='Закрыть', callback_data='cancel')
instruction_btn = InlineKeyboardButton(text='Инструкция по боту',
                                       callback_data='instruction',
                                       url="https://t.me/develop_python_ub/130")
developer_btn = InlineKeyboardButton(text="Разработчик",
                                     callback_data='dev')

choice.add(download_btn)
choice.add(schedule_btn)
choice.add(instruction_btn)
choice.add(developer_btn, cancel_btn)
