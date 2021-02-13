import os

from PIL import Image

from exceptions import NotCroppedImg
from my_logging import logger


@logger.catch
def cropped_img():
    """Обрезает изображение"""
    try:
        image = Image.open('schedule/schedule.png')
        if not os.path.exists('schedule/schedule.png'):
            logger.error('NO img schedule')
        cropped = image.crop((568, 543, 681, 711))
        cropped.save('schedule/schedule2.png')
        logger.info("Изображение успешно обрезано")
    except NotCroppedImg:
        raise NotCroppedImg("not cropped image")
