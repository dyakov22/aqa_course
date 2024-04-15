# - ImportError: виникає, коли імпортований модуль не може бути знайдений.

# from lesson_3 import new

# Exception

# - Exception: базовий клас для більшості вбудованих винятків.


# - IOError: виникає при виникненні помилки вводу/виводу (тепер замінений на OSError).


# - AttributeError: виникає, коли атрибут об'єкта не знайдено.

# class Today:
#
#     hour = 19
#     pass
#
# print(Today.minute)

# string = 'string'
# string.lower()
# string.new()


# - IndexError: виникає при спробі доступу до індексу за межами списку.

# l = [1, 2, 3]
#
# print(l[3])


# - KeyError: виникає при спробі доступу до ключа словника, який не існує.

# d = {'key': 'value'}

# print(d['key_2'])
# print(d.get('key_2', 'Такого ключа не існує'))


# - NameError: виникає, коли локальна або глобальна ім'я не знайдено.

# our_variable = 1
#
# print(our_variable_second)

# - SyntaxError: виникає, коли інтерпретатор зіткнувся з синтаксичною помилкою.

# counter = 0
# while counter < 10:
#     print(1)
#     counter += 1


# - ZeroDivisionError: виникає при спробі ділення на нуль.

# x = 10 / 0

# - TypeError: виникає при спробі операції з об'єктом неправильного типу.

# print('10' + 10)

# print('10' in 20)

# - ValueError: виникає, коли функція отримує аргумент правильного типу, але з неприпустимим значенням.

# print('Hello!'.index("q"))


x = 10


# try:
#     # 'Hello!'.index("q")
#     d = {'key': 'value'}
#     res = d['key2']
# except ValueError as error:
#     print('ValueError happened')
# except KeyError as error:
#     print(f'KeyError happened {error.__repr__()}')
# else:
#     print('Everything was ok!')
# finally:
#     print('from finally')
#
# def make_some_changes_with_db():
#     try:
#         print('connect to DB')
#         print('Execute db command')
#
#         # db_connection = SQLite(username, pwd)    connect to DB
#         # db_connection.flush()
#         'Hello!'.index("q")
#     except ValueError as error:
#         print(f'ValueError happened {error}')
#     return 1
#     # finally:
#     #     print('Close connection to DB')
#
#
# counter = 0
# counter += make_some_changes_with_db()
# counter += make_some_changes_with_db()
#
# print(f'{counter} connections are still open to DB')

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException




# try:
#     d = {1: 2}
#     d[2]   # Буде помилка
#
# #   print('after exception')  # Цей код не буде виконуватись через помилку вище
#
# except Exception as error:
#     print(error.__repr__())



# try:
#     result = 10 / 0
# except ZeroDivisionError as error:
#     print('Please do not divide by zero')
#
# print('Thanks for using our calculator')
#
# try:
#     result = 10 / 0
# except KeyError:
#     print('Please do not divide by zero')
# except ZeroDivisionError:
#     print('Please do not divide by zero')
# except Exception as e:
#     print(e)
# finally:
#     print('Thanks for using our calculator')
#
# print('Im out from try')
#
# def func1():
#     pass
#
# def func2():
#     raise ZeroDivisionError
#
#
# def main():
#     func1()
#     func2()
#
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyError as e:
#         pass
#     finally:
#         pass
