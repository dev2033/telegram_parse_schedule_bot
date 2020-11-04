"""
Файл для логирования
Используется библиотека loguru
"""
from loguru import logger


logger.add(
    "logging/debug.json",
    format="{level} {message}",
    level="DEBUG",
    rotation="2 MB",
    compression="zip",
    serialize=True
)
