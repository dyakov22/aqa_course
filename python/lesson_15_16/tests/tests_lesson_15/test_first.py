# def multiply(x: int):
#     return x ** 2
#
#
# def test_multiply():
#     actual = multiply(10)
#     expected = 1001
#     assert actual == expected, f'Expect return from multiply is {expected}, actual was {actual}'
#
import pytest


class TestClass:

    @classmethod
    def setup_class(self):
        print(f'Setup class')

    def setup_method(self):
        # self.actual = multiply(10)
        print(f'Setup method')

    def test_multiply(self):
        # expected = 100
        # assert self.actual == expected, f'Expect return from multiply is {expected}, actual was {self.actual} from class'
        print('First test case')
        assert True

    def teardown_method(self):
        print(f'Teardown method')

    @classmethod
    def teardown_class(self):
        print(f'Teardown class')


@pytest.mark.usefixtures('setup_class_fixture')
# @pytest.mark.usefixtures('setup_class_fixture', 'setup_method_fixture')
class TestClassFixture:

    def test_method_1(self, setup_method_fixture):
        print('From Test class 1')

    def test_method_2(self, setup_method_fixture):
        print('From Test class 2')