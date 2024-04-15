# class MyClass:
#
#     def __init__(self, value: int = 10):
#         self.value = value
#
#     def multiply(self) -> None:
#         # return self.value * 2
#         print(self.value * 2)
#
#
# # my_class = MyClass(value=20)
# #
# # print(my_class.multiply())
# #
# # print(f'from class {my_class.value}')
#
# my_class = MyClass()
# MyClass.multiply(my_class)
from typing import Optional


#  Attributes
# Encapsulation

# class MyClass:
#     class_value = 20
#
#     def __init__(self, value: int, bridge: int, tree: str):
#         self.value = value  # attr of instance -> my_class = MyClass()
#
#         self._bridge = bridge
#
#         self.__tree = tree
#
#     def multiply(self) -> None:
#         # return self.value * 2
#         print(self.value * 2)
#
#
# my_class = MyClass(15, 999, 'maple')
#
# my_class._bridge
#
# # print(my_class.__tree)
#
# print(my_class._MyClass__tree)
#
# my_class._MyClass__tree = 1
#
# print(my_class._MyClass__tree)
#
# # print(dir(my_class))
#
#
#
# # print(my_class.value)
# #
# # my_class.value = 100000000
# #
# # print(my_class.value)
# #
# # print(my_class._bridge)
# #
# # my_class._bridge = 10
# #
# # print(my_class._bridge)
#
# # print(MyClass.class_value)


class Weather:  # == class Weather(object)

    def __init__(self, country: str):
        self.country = country

        # if country.lower() in ['usa', 'canada'] and not degree_type:

        if country.lower() in ['usa', 'canada']:
            self.degree_type = 'F'
        else:
            self.degree_type = 'C'
            # self.degree_type = degree_type


# Getter, Setter, Deleter

class ATM:

    def __init__(self, exchange_rate: int | float, amount: int):
        self.__exchange_rate = exchange_rate
        self.__amount = amount

    def withdraw(self, withdraw_amount):
        if self.amount < withdraw_amount:
            self.emergency_call()
            return False
        self.__amount -= withdraw_amount
        # return withdraw_amount
        print(f'Withdraw {withdraw_amount}')

    @property
    def amount(self):
        """
        отримати залишок у банкоматі
        :return: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        """
        додати гроші до банкомату (self.__amount)
        :param value: Accept int and should be higher than 0 and not higher than 1000000
        :return: None
        """
        if value <= 0:
            raise ValueError('Amount could not be less than 0')
        elif value >= 1000000:
            raise ValueError('ATM does not have enough space')
        else:
            self.__amount = value

    @amount.deleter
    def amount(self):
        """
        зупиняэмо роботу банкомату
        :return:
        """
        del self.__amount

    def emergency_call(self) -> None:
        """
        Call to staff and let them know that money are over
        :return:
        """
        if self.amount < 1000:
            print('Call !!!!!!!!!!!!!!!!')
        else:
            print('Please withdraw less money')


atm = ATM(40, 10000)


(atm.withdraw(100000000))

print(atm.amount)

(atm.withdraw(9000))

# next client

print(atm.amount)

(atm.withdraw(1000))

(atm.withdraw(1000))

atm.amount = 10000

(atm.withdraw(1000))

# atm.amount

del atm.amount


atm.withdraw(1)


#
# def set_amount(self, value):
#     if value <= 0:
#         raise ValueError('Amount could not be less than 0')
#     elif value >= 1000000:
#         raise ValueError('ATM does not have enough space')
#     else:
#         self.__amount = value


# def set_amount(self, s_amount: int):
#     self.__amount = s_amount
#



# d = {'country': 'Ukraine'}
#
#
# d['country'] = 'Canada'
#
#
# print(d['country'])
#
# def amount():
#     print(1)
#
#
# def amount():
#     print(2)
#
#
# amount()

class ClassExample:

    class_list = [2]

    def __init__(self, value):
        self.instance_list = [value]


cls1 = ClassExample(100)
cls2 = ClassExample(200)
cls3 = ClassExample(300)

cls2.class_list.append('ansdjkjnadkjasdasdad')

# ClassExample.class_list.append(100000)

print(f'{cls1.class_list} cls1 class')
print(f'{cls1.instance_list} cls1 init')

# cls1.instance_list.append(1)
# cls1.class_list.append(1)

print(f'{cls2.class_list} cls2 class')
print(f'{cls2.instance_list} cls2 init')

print(f'{cls3.class_list} cls3 class')
print(f'{cls3.instance_list} cls3 init')