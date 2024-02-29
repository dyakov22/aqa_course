# Immutable

# int

integer = 10
integer_1 = 20

# print(integer)
# print(integer_1)

# print('Sum of integer & integer_1 is equal to:', integer + integer_1, sep='\n', end=' Im from end')

# print(id(integer))
# print(id(integer_1))

integer = integer + integer_1

# print(id(integer))

# float

floating = 10.02
floating2 = 10.2222222222222222222222
# print(floating.is_integer())

# str

string = 'it\'s a string'

string1 = "it's a string"

# tuple

tuple_1 = (1, 2, 'string', [{'key_1': 'value'}])
#  index   0  1     2                3

# print(tuple_1.index(1))

# Mutable

# list

list_1 = [1, 2, 'string', [{'key_1': 'value'}]]
# index   0  1     2                3


# print(list_1)
# print(id(list_1))

list_1.append('new_value')

# print(list_1)
# print(id(list_1))


# dict

dictionary = {'country': 'Ukraine', 'city': 'kiyv', 'additional_info': {'street': 'Maidan', 'build number': 13021}}
print(dictionary)

dictionary['city'] = 'Kharkiv'
print(dictionary)


dictionary['additional_info']['street'] = 'Privokzalna'

print(dictionary)

dictionary['floor'] = 10
print(dictionary)

# set

set_1 = {1, 2, 3, 4, 4}

print(set_1[1])

dictionary[frozenset([1,2,3])] = 'string'


s = ''

# print(s)