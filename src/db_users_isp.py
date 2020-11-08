import sqlite3

from my_logging import logger


conn = sqlite3.connect("db_dir/users.db")
cursor = conn.cursor()

# Создание БД
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users 
    (user_id INTEGER, first_name TEXT, last_name TEXT, user_name TEXT)
    """
)


def add_data_db(user_id, first_name, last_name, user_name):
    """
    Добавляет пользоваетеля в базу данных и проверяет:
        если он есть в БД, то не добавлять
    """
    dict_arg = [(user_id, first_name, last_name, user_name)]
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id, ))
    check1 = cursor.fetchall()
    if not check1:
        cursor.executemany('INSERT INTO users VALUES(?,?,?,?)', dict_arg)
    else:
        logger.info("Пользователь уже зарегистрован в базе данных")
    conn.commit()


conn.commit()

