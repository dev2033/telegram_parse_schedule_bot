"""Кнопки для бота"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


nagib = InlineKeyboardMarkup()
spam_key = InlineKeyboardMarkup()
choice = InlineKeyboardMarkup()


download_btn = InlineKeyboardButton(text='Скачать расписание',
                                    callback_data='download')
schedule_btn = InlineKeyboardButton(text='Прислать расписание',
                                    callback_data='schedule')
cancel_btn = InlineKeyboardButton(text='Закрыть', callback_data='cancel')
instruction_btn = InlineKeyboardButton(text='Инструкция по боту',
                                       callback_data='instruction',
                                       url='https://t.me/develop_python_ub/130')
developer_btn = InlineKeyboardButton(text='Разработчик',
                                     callback_data='dev')
registration = InlineKeyboardButton(text='Регистрация',
                                    callback_data='reg')


# first = InlineKeyboardButton(text='1 клава', callback_data='phone')
# second = InlineKeyboardButton(text='2 клава', callback_data='phone2')
# three = InlineKeyboardButton(text='3 клава', callback_data='phone3')
#
# one = InlineKeyboardButton(text='Придурки', callback_data='phone4')
#
#
# nagib.add(one)
#
# spam_key.add(first, second)

choice.add(download_btn)
choice.add(schedule_btn)
choice.add(instruction_btn)
choice.add(developer_btn, registration)
choice.add(cancel_btn)
