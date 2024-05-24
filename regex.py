# ''.find()
#
# ''.split()
#
# ''.replace()


import re

# testable_str = 'Hello!2'


# match = re.match(r'Hello', testable_str)
#
# print(match)


# testable_str = 'Hello'
#
#
# full_match = re.fullmatch('Hello', testable_str)
#
# print(full_match)


# testable_str = 'elloHHHHHHHH'
#
#
# find_all = re.findall('H', testable_str)  # -> list
#
# print(find_all)


# testable_str = 'elloHHHHHHHH'
#
# find_iter = re.finditer('H', testable_str)  # -> iter
#
# print(find_iter)
# for i in find_iter:
#     print(i)


# testable_str = 'elloHHHHHHHH'
#
#
# search = re.search('H', testable_str)
#
# print(search)


# testable_str = 'elloHHHHHHHH'


# replace = re.sub('H', '@', testable_str, count=2)
#
#
# print(replace)


# replace_n = re.subn('H', '@', testable_str)  # -> tuple
#
# print(replace_n)

#
# testable_str = 'elloHHHHLHHaHH'
#
#
# split = re.split('H', testable_str, maxsplit=3)
#
# print(testable_str.split('H', 3))
#
# print(split)


text = '''
How to use the tables
The tables are meant to serve as an accelerated regex course, and they are meant to be read slowly, one line at a time.
 On each line, in the leftmost column, you will find a new element of regex syntax. The next column, "Legend", explains 
 what the element means (or encodes) in the regex syntax. The next two columns work hand in hand: the "Example" column 
 gives a valid regular expression that uses the eleme8nt, and the "Sample Match" column presents a text string that could 
 be matched by the regular expression.

You can read the tables online, of course, but if you suffer from even the mildest case of online-ADD (attention deficit 
disorder), like most of us… Well then, I highly recommend you print them out. You'll be able to study them slowly, and 
to use them as a cheat sheet later, when you are reading the rest of the site or experimenting with your own regular 
expressions
'''

# result = re.findall(r'\S', text)
#
# # print(result)
#
# text = 'How to use the 12810231 tables j'
#
# result = re.findall(r'\d{5}', text)
#
# print(result)


# text = 'taele to use the 12810231 tables '
#
# result = re.findall(r'ta.le', text)
#
# print(result)


# text = 'taele to use the 12810231 tables '
#
# result = re.findall(r'^\w+\s', text)
#
# print(result)

# text = 'taele to use the 12810231 tables '
#
# result = re.findall(r'tables\s{2}$', text)
#
# print(result)
#
#
#
# text = 'taele to use the 12810231 tables '
#
# result = re.findall(r'12*', text)
#
# print(result)
#
#
# text = 'taele to use the 1281023128 tables '
#
# result = re.findall(r'12|28', text)
#
# print(result)
#
# text = 'taelE .to use the 1281023128 tables '
#
# result = re.findall(r'taele .to', text, flags=re.IGNORECASE)
#
# print(result)

# re.IGNORECASE


# while True:
#
#     input_value = input('Enter email: ')
#
#     res = re.match(r'/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/', input_value)
#
#
#     if res:
#         print(res.group())
#         break
#     continue


