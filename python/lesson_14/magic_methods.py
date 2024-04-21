
'''
- __add__(self, other): Сложение +.
- __sub__(self, other): Вычитание -.
- __mul__(self, other): Умножение .
- __truediv__(self, other): Деление .
- __floordiv__(self, other): Целочисленное деление /.
- __mod__(self, other): Остаток от деления %.
- __pow__(self, other): Возведение в степень *.
'''
from typing import Union


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Point(self.x + other[0], self.y + other[1])
        else:
            raise TypeError('Uns type')

    # def __str__(self):
    #     return f'Point has 2 args x and y with values {self.x} & {self.y}'

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


#
# point_one = Point(1, 2)
# point_two = Point(10, 20)
#
# point_three = point_one + point_two
#
# var = repr(point_three)
# print(var)
# point_four = point_one + (1, 2)
#
# print(point_four)
# print(point_four.__str__())
#
# # point_four = point_one + (1, 2, 2)
#
#


class ContextManager:

    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(file=self.file_path, mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print('Context manager executed with error')
        self.file.close()

#
# path = '/Users/ndiakov/PycharmProjects/aqa_courae/lesson_13/abstact_classes.py'
#
# with ContextManager(file_path=path, mode='r') as file:
#     raise FileNotFoundError('File was not found')
#     print(file.readlines())
#
#


class CallClass:

    def __call__(self, *args, **kwargs):
        print('Our class was called')

#
# call_class = CallClass()
# call_class()




'''
- __eq__(self, other): Определяет поведение оператора равенства ==.
- __ne__(self, other): Определяет поведение оператора неравенства !=.
- __lt__(self, other): Меньше <.
- __le__(self, other): Меньше или равно <=.
- __gt__(self, other): Больше >.
- __ge__(self, other): Больше или равно >=.
'''

class Equal:

    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        else:
            raise Exception('Other data types than INT are not acceptable')


# equal = Equal(10)
# # print(equal == '10')
# print(equal == 10)
# print(equal == 11)


class Len:

    def __init__(self, value: Union[list, tuple]):
        self.value = value

    def add_arg_to_value_attr(self, arg):
        if isinstance(self.value, list):
            self.value.append(arg)
        else:
            print('Sorry!')

    def __len__(self):
        return len(self.value)

#
# len_class = Len([1000, 12, 321, 412, 412, 241])
# len_class_1 = Len((1000, 12, 321, 412, 412, 241))
#
# len_class.add_arg_to_value_attr(20)
# len_class_1.add_arg_to_value_attr(20)
#
# print(len(len_class))
# print(len(len_class_1))


class CallClass:

    def __call__(self, *args, **kwargs):
        print('Our class was called')


call_class = CallClass()

call_class()
