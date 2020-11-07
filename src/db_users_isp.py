import sqlite3

from my_logging import logger
from bot import user_registration


conn = sqlite3.connect("db_pack/users.db")
cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users 
    (user_id INTEGER, first_name TEXT, last_name TEXT, user_name TEXT)
    """
)


def add_data_db(user_id, first_name, last_name, user_name):
    dict_arg = [(user_id, first_name, last_name, user_name)]
    cursor.executemany(
        """
        INSERT INTO users(user_id, first_name, last_name, user_name) 
        VALUES (?, ?, ?, ?)
        """, dict_arg)
    conn.commit()


conn.commit()

