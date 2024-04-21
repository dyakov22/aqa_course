# 1. os.chdir(path) - Змінює поточний робочий каталог на вказаний шлях.
# 2. os.getcwd() - Повертає рядок, що представляє поточний робочий каталог.
# 3. os.listdir(path='.') - Повертає список усіх файлів та каталогів у вказаному каталозі.
# 4. os.mkdir(path, mode=0o777) - Створює каталог за вказаним шляхом.
# 5. os.makedirs(name, mode=0o777, exist_ok=False) - Рекурсивно створює каталоги вказані в шляху; створює всі проміжні каталоги,
# необхідні для створення кінцевого каталогу.
# 6. os.remove(path) - Видаляє файл за вказаним шляхом.
# 7. os.rename(src, dst) - Перейменовує файл або каталог з src на dst.
# 8. os.rmdir(path) - Видаляє пустий каталог.
# 9. os.removedirs(name) - Рекурсивно видаляє каталоги, закінчуючи вказаним іменем; продовжує видалення вгору по дереву, поки не зустріне непустий каталог.
# 10. os.system(command) - Виконує системну команду.
# 11. os.path.join(path, *paths) - Об'єднує один або декілька компонентів шляху з урахуванням особливостей операційної системи.
# 12. os.path.split(path) - Розділяє шлях на кортеж, що складається з двох частин: голови та хвоста, де хвіст - останній компонент шляху.
# 13. os.path.dirname(path) - Повертає директорію, що містить файл або кінцеву директорію в шляху.
# 14. os.path.basename(path) - Повертає базове ім'я шляху (останній компонент шляху).
# 15. os.path.exists(path) - Перевіряє, чи існує вказаний шлях або об'єкт.
# 16. os.path.isfile(path) - Перевіряє, чи є вказаний шлях файлом.
# 17. os.path.isdir(path) - Перевіряє, чи є вказаний шлях директорією.
# 18. os.getenv(key, default=None) - Повертає значення змінної оточення або default, якщо змінна не встановлена.
# 19. os.putenv(key, value) - Встановлює значення змінної оточення.
# 20. os.rename() - Зміна імена та можливість перести файл
# 21. os.replace()
# 22. os.path.abspath(path)


import os


# print(os.getcwd())
#
# os.chdir('../')
#
# print(os.getcwd())


# print(os.getcwd())
# os.mkdir('temp/temp_1')
# os.makedirs('temp/temp_1/temp_2')

# os.rmdir('temp/temp_1/temp_2')

# os.remove('temp/temp.txt')

# os.unlink('temp/temp1.txt')

# os.removedirs('temp/temp_1')

# PATH

# print(__file__)
# '/Users/ndiakov/PycharmProjects/aqa_courae/lesson_8/os_path.py'
# '/Users/ndiakov/PycharmProjects/aqa_courae/lesson_8/os_path.py'

# print(os.path.dirname(__file__))

def install_app():
    print('App is installing.....')


#
# app_name = 'app.ipa'
# # download_app()  we are going to download to dir with our file
#
# dir_name = os.path.dirname(__file__)
# print('Dir name: ', dir_name)
#
# full_path = os.path.join(dir_name, app_name)
#
# print(full_path)

# if os.path.exists(full_path):
#     install_app()
#
# else:
#     print('Hm.... file was not found')

# print('IS DIR')
# print('Check if dir ', os.path.isdir(dir_name))
# print('Check if file ', os.path.isfile(dir_name), end='\n')
#
# print('IS FILE')
# print('Check if dir ', os.path.isdir(__file__))
# print('Check if file ', os.path.isfile(__file__), end='\n')

# dir_name = os.path.dirname(__file__)


# result = os.path.split(__file__)


# result = os.path.split(dir_name)

# print(result)


# print(os.path.basename(__file__))


# print(os.path.abspath(''))
# '/Users/ndiakov/PycharmProjects/aqa_courae/lesson_8' -> run file

# '/Users/ndiakov/PycharmProjects/aqa_courae' -> run from project root dir


# dir_name = os.path.dirname(__file__)
#
# jks_file = os.path.join(dir_name, 'config.jks')
# aab_file = os.path.join(dir_name, 'aab.jks')
# apk_file = os.path.join(dir_name, 'apk.jks')
#
#
#
# if os.path.exists(apk_file):
#     install_app()
# elif os.path.exists(aab_file):
#     print('Prepare app convert from aab to apk')
#     install_app()
# else:
#     print('Download aab')
#     print('Prepare app convert from aab to apk')
#     install_app()


# print(os.getenv('PATH'))

# os.putenv('key1', 'value')

# print(os.getenv('key'))


# print(eval("{'key': 'value'}").get('key'))
#
# for dirpath, dirnames, filenames in os.walk('../'):
#     if 'venv' not in dirpath:
#         print(dirpath)
#         print(dirnames)
#         print(filenames)

#
#
# import os
#
#
# print(__file__)
#
# path = os.path.dirname(__file__)
# print(path)
#
# main_dir = '/Users/ndiakov'
#
# result_file = os.path.join(main_dir, 'text', 'text.txt')
#
#
# def main(path: str, *args):
#     for arg in args:
#         path += '/' + arg # f'/{arg}'}
#     return path
#
#
# res = main(main_dir, 'text', 'text.txt')
#
# # assert result_file == res
#
#
#
#
#
# with open('result_for_demonstration.csv', 'w') as file:
#     file.write(",Jan,Feb,Mar")
#     file.write("Employee1,1000,1000,1000")





