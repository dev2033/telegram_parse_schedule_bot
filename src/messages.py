"""
Руководство по боту
Команда /help
"""
from aiogram.utils.markdown import text, bold, italic, code


download_sch_msg_1 = "/download"
download_sch_msg_2 = text(code("команда которая загружает картинку с "
                               "расписанием 📜"))
schedule_img_msg_1 = "/photo"
schedule_img_msg_2 = text(code("команда, с помощью которой я могу "
                               "скинуть тебе расписание 📲"))

start_msg_1 = "/start"
start_msg_2 = text(code("Начинает работу с ботом 📱"))

name = "Danil"
link_vk = "https://vk.com/d.otzgig"
link_tg = "https://t.me/dev001010"
info_developer_msg_1 = "Информация о разработчике"
info_developer_msg_2 = f"Имя: {name}\n" \
                       f"ВК: {link_vk}\n" \
                       f"Telegram: {link_tg}"

