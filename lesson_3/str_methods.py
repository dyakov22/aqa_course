

# x = 10.9321
# y = 12
# 
# 
# # result = '{number1:<20}x is equal to {number2}'.format(number1=x, number2=y)
# 
# 
# result = 'x is equal to {}'.format(x)
# 
# 
# result_f = f'{y}x is equal to {x:.2f}'
# 
# print(result)
# print(result_f)
#
# - capitalize()

# string = 'hello mark'
# print(string.capitalize())



# - upper()

# print(string.upper())

# - lower()

# - strip()
# string = '  hello mark'
#
# print(string.strip('rk'))
# print(string)

# - lstrip(chars)
# - rstrip(chars)
# string = '  hello mark   '
# print(string.rstrip())


# - split(sep=None)

# string_for_split = 'Nikita,Diakov,27,Kiev'
# print(string_for_split.split(',', 2))


# - join(iterable)

# - replace(old, new, count)

string_for_split = 'Nikita,Diakov,27,Kiev'
# print(string_for_split.replace(',', '|'))


# - find(sub, start, end)

# print(string_for_split.find('27', 0, 5))

# - count(sub, start, end)


# - endswith(suffix, start, end)
# - startswith(prefix, start, end)

# print(string_for_split.startswith('N'))


# - index(sub, start, end)
# - swapcase()

# print(string_for_split.swapcase())
# - title()
# - isdigit()

my_number = '10'

print(my_number.isdigit())

# - islower()
# - isupper()
# - isspace()
# - isalnum()
# - isalpha()
# - istitle()
#

# - zfill(width)
# - casefold()
# - center(width[, fillchar])
# - expandtabs(tabsize=8)
# - ljust(width[, fillchar])
# - rjust(width[, fillchar])
# - partition(sep)
# - rpartition(sep)
# - splitlines([keepends])



# Slicing with string


string = 'My favorite string'

print(string[1:5])
print(string[::-1])  # розвернути рядок
print(string[-2])  # вивести другий елемент з кінця
