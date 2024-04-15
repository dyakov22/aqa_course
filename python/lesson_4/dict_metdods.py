# # key must be immutable str, int, float, frozenset, tuple
# # dict - hash map
#
# dictionary_1 = dict()
#
# print(dictionary_1)
#
# dictionary_2 = {}
#
# print(dictionary_2)
#
# dictionary_3 = {'date': 4, 'lesson_number': 'four', 10: 'int'}
#
# print(dictionary_3)
#
# dictionary_4 = dict(name='Nikita', date=4)
#
# print(dictionary_4)
#
# dictionary_5 = dict([('name', 'New'), ('age', 20)])
#
# print(dictionary_5)


# test_dict = {1: 'first', 1.0: 'second'}
# test_dict = {[1, 2]: 'first', 1.0: 'second'}
# test_dict = {[1, 2]: 'first', 1.0: 'second'}
# test_dict = {1: 'first', 1.9: 'second'}
# test_dict = {1.0: 'first', 1: 'second'}
# print(test_dict)

# print(hash(1))
# print(hash(2))

# dictionary_3 = {'date': 4, 'lesson_number': 'four'}

# print(dictionary_3['missed_key'])
# print(dictionary_3.get('missed_key', 'i know'))


# dictionary_3['new_key'] = 'new_value'

# dictionary_3.update(dictionary_5)

# print(dictionary_3)

#
# pair_of_deleted_value = dictionary_3.pop('date')
# pair_of_deleted_value_1 = dictionary_3.popitem()
#
# print(dictionary_3)
# print(pair_of_deleted_value)
# print(pair_of_deleted_value_1)

# print(list[dictionary_3.values()])
# print(tuple(dictionary_3.keys()))
# print(dictionary_3.items())