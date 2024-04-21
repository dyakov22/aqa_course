

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DB(metaclass=Singleton):

    def __init__(self, username: str, pwd: str):
        self.db_connection = f'{username}:{pwd}'

    def __enter__(self):
        return self.db_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Connection for {self.db_connection} was closed')

db1 = DB('username', 'pwd')

db2 = DB('username_1', 'pwd_2')
print(db2.db_connection)


# with DB('username', 'pwd') as user:
#     print(user)
#     ...
#
#     with DB('username_1', 'pwd_1') as second_user:
#         print(second_user)


def singleton(cls):
    _instances = {}

    def instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return instance


@singleton
class DB:

    def __init__(self, username: str, pwd: str):
        self.db_connection = f'{username}:{pwd}'

    def __enter__(self):
        return self.db_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Connection for {self.db_connection} was closed')

    def __del__(self):
        print('Bye-bye')


# db1 = DB('username', 'pwd')
#
# db2 = DB('username_2', 'pwd_2')

# print(f'Are these instances same {db1 is db2}')
# print(db2.db_connection)
#
# del db1
# del db2


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    @classmethod
    def reset_instance(cls, class_type):
        cls._instances.clear()
        # or
        # if class_type in cls._instances:
        #     del cls._instances[class_type]


class DB(metaclass=Singleton):
    def __init__(self, username: str, pwd: str):
        self.username = username
        self.pwd = pwd
        self.db_connection = f'{username}:{pwd}'

    def __enter__(self):
        return self.db_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Connection for {self.db_connection} was closed')


db_instance = DB("username", "password")
print(db_instance.db_connection)

Singleton.reset_instance(DB)

new_db_instance = DB("username_1", "password_1")
print(new_db_instance.db_connection)
