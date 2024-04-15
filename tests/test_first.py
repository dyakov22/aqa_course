# def multiply(x: int):
#     return x ** 2
#
#
# def test_multiply():
#     actual = multiply(10)
#     expected = 1001
#     assert actual == expected, f'Expect return from multiply is {expected}, actual was {actual}'
#
#
# class TestClass:
#
#     @classmethod
#     def setup_class(self):
#         print(f'Setup class')
#
#     def setup_method(self):
#         # self.actual = multiply(10)
#         print(f'Setup method')
#
#     def test_multiply(self):
#         # expected = 100
#         # assert self.actual == expected, f'Expect return from multiply is {expected}, actual was {self.actual} from class'
#         print('First test case')
#         assert True
#
#     def teardown_method(self):
#         print(f'Teardown method')
#
#     @classmethod
#     def teardown_class(self):
#         print(f'Teardown class')
