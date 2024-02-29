# str

my_string = 'my_string'
my_string_2 = str()

# print(my_string[1])

# print(my_string)
# print(my_string_2, 'string1', end='***')


# int

integer = 10
integer_1 = int()


# print(integer)
# print(id(integer))
# integer += 10
# print(integer)
# print(id(integer))



# print(integer_1)

# float

floating = 10.000006
floating_1 = float()

# print(floating_1)
# print(floating)


# list

list_1 = [1, 2, 3]
list_2 = list()


# print(id(list_1))
#
# list_1.append('new_value')
# list_1[1] = 'our new value'
#
# print(list_1)
# print(id(list_1))


# tuple

tuple_1 = (1, 2, 3)
tuple_2 = tuple()

list_3 = list(tuple_1)
list_3.extend('our second lesson')
tuple_1 = tuple(list_3)
# print(isinstance(tuple_1, tuple))

# print(tuple_1)
# print(tuple_2)

# dict

dictionary = {10: 80, 'city': 'Kiev'}
dictionary_1 = dict()

# print(id(dictionary))
#
# dictionary['country'] = 'Ukraine'
# print(id(dictionary))
#
# print(dictionary)
# print(dictionary_1)


# set

# set_1 = {1, 2, 3}
# set_1 = {3, 2, 1}
set_1 = {'Y', 'R', 'A', 'B'}
# set_2 = set([1, 2, 3])
#
# set_1.add(3)
# set_1.add(2)
# set_1.add(1)

# print(set_1)
# print(set_2)


# frozenset

frozenset_1 = frozenset([1, 2, 34])


# bool

am_i_human = True  #  is_true = 1
am_i_dog = False  #  is_false = 0

is_true = 1
is_false = 0


is_true_1 = "string"
is_false_2 = ""
# is_false_2 = str()



# Mutable
# list
# set
# dict


# Immutable
# int
# str
# float
# tuple


# Ordered/Упорядковані
# list
# tuple
# str


# Unordered
# set


import sys


l = [1, 2, 3]
t = (1, 2, 3)

print('List', sys.getsizeof(l), sep='=')
print('Tuple', sys.getsizeof(t), sep='=')










