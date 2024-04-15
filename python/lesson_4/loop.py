import time

# [a, b, c, d]
#  1  2  3  4

# word
# 1234



dictionary = {'date': 4, 'lesson_number': 'four', 10: 'int'}
#
# for value in dictionary.values():
#     print(value)
#
#
# for value in dictionary.keys():
#     print(value)


# for key, value in dictionary.items():
#     print('key', key)
#     print('value', value)


# list_of_elements = find_elements('locator')
#
# dict_elements = {'element_1': 'text', 'element_2': 'our word'}


# for key, value in dict_elements.items():
#     if value == 'our word':
#         print(key)
#
# for key, value in [(1, 'first'), (2, 'second')]:
#     if value == 'second':
#         print(key)


# list_1 = ['Anna', 'Kostya', 'Vadym']
# dictionary_1 = {}
# for index, value in enumerate(list_1):
#     dictionary_1[value] = index
#     #
#     # print('index', index)
#     # print('value', value)
#
# q = enumerate(list_1)
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
#
#
# print(dictionary_1)


# get data from DB
# string = ['my string', 'new', 'test data', 1, 2, 3, 4]
#
# for index, letter in enumerate(string):
#     if letter != 'new':
#         print(f'index of {letter} is {index}')
#     elif letter == 'test data':
#         break
#     string.pop()
#
# else:
#     for s in string:
#         print(f'db.commit({s})')
#     print('db.close()')



# boolean = True

# counter = 0


# while counter < 10:
#     print('Im from while')
#     counter += 1
#
# print('out from while')


# while True:
#
#     number_1 = int(input('number 1: '))
#     number_2 = int(input('number 2: '))
#     operator = input('operator: ')
#
#     if operator == '+':
#         print(number_1 + number_2)
#     elif operator == '/':
#         if number_2 == 0:
#             print('You entered wrong value')
#             continue
#         else:
#             print(number_1 / number_2)
#
#     break
#
#
# print('out of while')

# counter = 0
#
#
# while counter < 10:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         break
# else:
#     print('I did not see break in while ')


# list comprehension

# l = []
#
# for i in range(10):
#     if i % 2 == 0:
#         l.append(i)
#
# print(l)
#
# l1 = [i for i in range(10) if i % 2 == 0]
l1 = [i for i in range(10)]


new_str = ''.join([s for s in 'bbasiudbIBAIBASDIFBASjsdnfsjkdfnKJSDNFKJSDF' if s.isupper()])

print(new_str)

# print(l1)
#
# l2 = [True for i in range(10) if i % 2 == 0]
#
# print(l1)
#
# print(l2)


# dict comprehension

# d = {key: key / 10 for key in range(100, 120) if (key + 90) < 200}

# print(d)


