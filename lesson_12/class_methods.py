#
#
# class ATM:
#
#     class_attr = []
#
#     def __init__(self, name: str, balance: int = 10000):
#         self.balance = balance
#         self.bank_name = name
#         self.__pin = (9431, 1111, 222212)
#
#     def give_money_to_customer(self, amount: int, customer_pin: int) -> int:
#         if self.check_if_amount_is_int(amount):
#             if customer_pin in self.__pin:
#                 return self._get_money(amount=amount)
#
#             else:
#                 print('Access denied')
#
#     def _get_money(self, amount: int):
#         if self.balance >= amount:
#             self.balance -= amount
#             return amount
#
#     def __new_balance(self, is_admin: bool, amount: int):
#         if is_admin:
#             self.balance = amount
#
#     @staticmethod  # допоміжна функція
#     def check_if_amount_is_int(amount: int):
#         if isinstance(amount, int):
#             return True
#
#     @classmethod
#     def check_pin(cls):
#         pass
#
#
# atm_instance = ATM('Privat')
#
# # atm_instance.print_bank_name()
#
# # atm_instance.check_if_amount_is_int(10)
#
#
# # ATM.check_if_amount_is_int(10)
#
# # print(atm_instance.give_money_to_customer(amount=1, customer_pin=1111))
#
# # atm_instance.check_pin(1)
#
# ATM.check_pin()





class Library:

    book_amount = 0

    def __init__(self, book_name: str, title: str):
        self.book_name = book_name
        self.title = title
        Library.book_amount += 1

    @staticmethod
    def check_title(title: str):
        if len(title) >= 3:
            return True
        else:
            return False

    @classmethod
    def get_book_amount(cls):
        return cls.book_amount

    def get_book(self):
        return f'Book name is {self.book_name}, title is {self.title}'


book = Library('Book1', 'title1')
book1 = Library('Book2', 'title2')
book2 = Library('Book3', 'title3')


print(Library.get_book_amount())











