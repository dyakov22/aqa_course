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
if False:
    pass

'git remote add origin git@github.com:dyakov22/test1.git'