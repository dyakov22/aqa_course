import sqlite3
import typing

from pathlib import PosixPath


class DBManagerSQLite:

    def __init__(self, path_to_db: typing.Union[str, PosixPath]):
        self.path_to_lib = path_to_db

    def __enter__(self):
        self.connection = sqlite3.connect(self.path_to_lib)
        self.cursor = self.connection.cursor()
        print('db connection was created')
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        print('db connection was closed')


# with DBManagerSQLite('/Users/ndiakov/PycharmProjects/aqa_courae/lessons/db/aqa_course_with_fk.db') as db_cursor:
#     db_cursor.execute('INSERT INTO users (name, age, email) VALUES ("name1", 100, "assssd@example.com")')
#     user_id = db_cursor.lastrowid
#     db_cursor.execute(f'INSERT INTO user_details (user_id, address, phone) VALUES ({user_id}, "address1", "3908312")')
#     db_cursor.connection.commit()


def read_from_db(path: str, execute_command='select * from users'):
    with DBManagerSQLite(path_to_db=path) as db_cursor:
        return db_cursor.execute(execute_command).fetchall()
