"""Удаляет расписание из папки"""
import os
import glob

from my_logging import logger


def remove():
    remove_schedule = glob.glob('schedule/schedule.png')
    remove_schedule2 = glob.glob('schedule/schedule2.png')
    for file in remove_schedule:
        try:
            os.remove(file)
            logger.info("Расписание удалено")
        except OSError:
            logger.warning('Не удалось удалить расписание')

    for file in remove_schedule2:
        try:
            os.remove(file)
        except OSError:
            logger.warning('Не удалось удалить расписание')


