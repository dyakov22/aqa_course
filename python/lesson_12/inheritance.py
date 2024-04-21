

class Character:

    def __init__(self, damage: int):
        self.health = 100
        self.damage = damage
        # print('from character')

    def is_alive(self):
        if self.health <= 0:
            return False

    def hit(self):
        return self.damage

    def is_death(self):
        if self.health <= 0:
            return True
        else:
            return False


class Warrior(Character):

    def __init__(self, damage: int):
        super().__init__(damage)

    def double_hit(self):
        return self.damage * 2

    def is_death(self):
        super().is_death()
        print('is death')


class Elf(Character):

    def double_hit(self):
        return self.damage * 2


# character = Character(10)

# warrior = Warrior(20)
#
# warrior.is_death()





# character.health = 10
#
# print(character.health)
#
# print(warrior.health)
#
#
# class A:
#
#     def __init__(self):
#         self.x = 10
#
#
# class B(A):
#
#     def __init__(self):
#         self.x = 20
#         super().__init__()
#
#
# class C:
#
#     def __init__(self):
#         self.x = 30
#         # super().__init__()
#
#
# class D(C, B):
#
#     def __init__(self):
#
#         super().__init__()
#         print(f'from D init {self.x}')
#
#     # def print_x(self):
#     #     print(f'print x {self.x}')
#
# d = D()
# # d.print_x()
# # print(getattr(d, 'x'))
#
# print(D.mro())


# <class '__main__.D'>,
# <class '__main__.C'>,
# <class '__main__.B'>,
# <class '__main__.A'>,
# <class 'object'>

# def get_atr():
#     for obj in []:   #[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]:
#         if getattr(obj, 'x'):
#             return getattr(obj, 'x')
#


