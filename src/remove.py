"""Удаляет расписание из папки"""
import os
import glob

from my_logging import logger


def remove():
    remove_schedule = glob.glob('schedule/*.png')
    for file in remove_schedule:
        try:
            os.remove(file)
            logger.info("Расписание удалено")
        except OSError:
            logger.warning('Не удалось удалить расписание')

