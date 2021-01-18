"""
Тут происходит парсинг картинки с расписанием
"""
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

from exceptions import NotSchedule
from my_logging import logger

import requests


url = "http://simfpolyteh.ru/raspisanie/"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) "
                  "AppleWebKit/604.1.34 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A5341f Safari/604.1 "
}

req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "lxml")


@logger.catch
def pars_img() -> None:
    """Скачивает картинку с сайта"""
    try:
        image = soup.find(class_="page_raspis_block_img").find("img").get("src")
        urlretrieve(image, filename="schedule/schedule.png")
        logger.info("Скачивание успешно завершено!")
    except NotSchedule:
        logger.warning("NOT schedule")
