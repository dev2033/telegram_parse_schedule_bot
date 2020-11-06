"""Кастомные исключения"""


class NotSchedule(Exception):
    """
    Исключения, которое отлавливается
    если нет картинки на сайте
    """
    pass


class NotCroppedImg(Exception):
    """
    Если не удалось обрезать картинку
    """
    pass
