"""Арифметичні"""

# +
# -
# *
# /
# // цілочислене
# % з остачею
# **
#
# x = 100
# y = 18
#
# print(y * 5)
# print(x % y)

my_str = 'Monday'

your_str = 'February'

# print(my_str - your_str)


"""
Присвоювання
"""

# - = Присвоювання
# - += Додавання з присвоюванням
# - -= Віднімання з присвоюванням
# - *= Множення з присвоюванням
# - /= Ділення з присвоюванням
# - %= Присвоювання залишку від ділення
# - **= Піднесення до степеня з присвоюванням
# - //= Ділення націло з присвоюванням


# x = 100
#
# x //= 51
# print(x)


"""Оператори порівняння"""

# - == Рівно
# - != Не рівно
# - > Більше ніж
# - < Менше ніж
# - >= Більше ніж або рівно
# - <= Менше ніж або рівно

#
# my_age = int(input('Enter your age: '))
# allow_enter = 18
# # my_current_age = 15
#
# if my_age >= allow_enter:
#     print('Enter allowed')
#
# elif my_age <= allow_enter:
#     print('Enter declined')
#
# else:
#     print('I do not know your age, enter disallowed')


"""Logical operators"""

# - and Повертає True, якщо обидва вирази є істинними
# - or Повертає True, якщо хоча б один з виразів є істинним
# - not Повертає заперечення виразу


# age = 18
# childhood_age = 6

# #  | True  |    |     True        |
# if age > 10 and childhood_age == 6:
#     print('Allow enter')
#
# else:
#     print('Im from else')


# #  | False  |    |     True        |
# if age < 10 or childhood_age == 6:
#     print('Allow enter')
#
# else:
#     print('Im from else')


# if not False:
#     print('Allow enter')
#
# else:
#     print('Im from else')


# is
# is not
#
# l = ['Laptop', 'Monitor', 'Mouse']
#
# list_1 = l
#
#
# if l is list_1:
#     print('YES')
# else:
#     print('NO')

# if l == ['Laptop', 'Monitor', 'Mouse']:
#     print('так ми однакові ')


'''Оператори членства'''

# in
# not in

#
# l = ['Laptop', 'Monitor', 'Mouse']
#
# # x = 10
#
# if 'Table' in l:
#     print('Table not in l')
# elif 'Chair' not in l:
#     print('Chair not in l')
# elif 'Monitor' in l:
#     print('Monitor in l')
# else:
#     print('nothing here')
#
# print('Im out of if')


# if 'вираз':
#     ''

x = 10

# match x:
#
#     case 9 | 10:  #  if/elif  | - or
#         print('Yes x is equal to 10 OR 9')
#     case 15:  #  if/elif
#         print('Yes x is equal to 15')
#     case _:
#         print('nothing from above')

# age = 59
# clothe_color = 'blue'
#
# match clothe_color:
#
#     case 'red':
#         print('out from here!')
#     case 'blue' if age in range(18, 60):
#         print('Yes clothe is blue and age is ok')
#     case _:
#         print('out from here! Im from default flow')
#
# for index in range(5, 50, 5):
#     print(index)

is_in = 10 in range(20)  # True
print(is_in)

if (2 in [1, 2, 3, 4]) == (2 in [1, 2, 3, 4]):  # if True:
    print('good')
else:
    print('bad')

# if starts -> (2 in [1, 2, 3, 4]) -> True -> print('good')
# if starts -> True -> print('good')


if True:
    print(
        ''
    )
