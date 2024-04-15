#
# class ATM:
#
#     def __init__(self):
#         self._amount = 1000
#
#
#     def show_amount(self):
#         print(self._amount)
#
#
# class MonoATM:
#
#     def __init__(self):
#         self._amount = 1000
#         # self.new = 0
#
#
#     def show_amount(self):
#         print(10)
#     #
#     # def cut_amount(self):
#     #     return self.new
#
#
# class Terminal(ATM, MonoATM):
#
#     def __init__(self):
#         super().__init__()
#
#
#     def show_amount(self):
#         MonoATM.show_amount(self)
#
#
#
#
#
# terminal = Terminal()
#
# terminal.cut_amount()
#
#
# Terminal.show_amount(terminal)
#
#
# class Character:
#
#     def __init__(self, race: str):
#         print('From Character')
#         self.race = race
#         super().__init__()
#
#
# class Shield:
#
#     def __init__(self):
#         print('From Shield')
#         self.health = 100
#         super().__init__()
#
#
# class Hero(Character, Shield):
#
#     # Variant 1 (DO NOT DO IT)
#     # def __init__(self, race: str):
#     #     Shield.__init__(self)
#     #     print('From Hero')
#     #     super().__init__(race)
#
#     def __init__(self, race: str):
#         print('From Hero')
#         super().__init__(race)
#
#
#
# hero = Hero('hero')
# # print(hero.health)
# print(Hero.mro())


#
# From Hero -> hero = Hero('hero') 1 -> super() -> init Character
# From Character 2  -> super() -> init Shield
# From Shield  -> super() -> init object
# [<class '__main__.Hero'>, <class '__main__.Character'>, <class '__main__.Shield'>, <class 'object'>]
#                     1                         2                            3
#
#


# class ATM:  == class ATM(object):



#  Polymorphism

class Car:  # parent class

    def start_engine(self):
        print('start Engine from Car class')

    def stop_engine(self):
        print('stop Engine from Car class')


class Fiat(Car):

    def start_engine(self):
        print('start Engine from FIAT class')

    def stop_engine(self):
        print('stop Engine from FIAT class')


class BMW(Car):

    def start_engine(self):
        print('start Engine from BMW class')

    def stop_engine(self):
        print('stop Engine from BMW class')


def start_engine(obj: Car):
    obj.start_engine()


# customer came

fiat = Fiat()
bmw = BMW()

for obj in [fiat, bmw]:
    start_engine(obj)
