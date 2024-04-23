import pytest

from python.lesson_15_16.src.calculator import Calculator

"""
CLI ARGUMENTS
-m - markers
-k - test function
pytest path to test_*.py file
"""


@pytest.mark.smoke
def test_divide_positive():
    calculator = Calculator(10, 1)
    assert calculator.divide() == 10


@pytest.mark.smoke
def test_divide_positive1():
    calculator = Calculator(10, 1)
    assert calculator.divide() == 10


@pytest.mark.regression
def test_divide_positive2():
    calculator = Calculator(10, 1)
    assert calculator.divide() == 10


@pytest.mark.regression
def test_divide_negative():
    calculator = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError, match=r'.* divide by 0') as error:
        assert calculator.divide() == 10
    print(error)


@pytest.mark.skip(reason='Feature did not implemented yet')
def test_multiply_positive_numbers_skip():
    calculator = Calculator(10, 0)
    assert calculator.multiply() == 0


@pytest.mark.skipif(True, reason='Feature did not implemented yet')
def test_multiply_negative_numbers_skip_if():
    calculator = Calculator(10, -10)
    assert calculator.multiply() == -100


@pytest.mark.xfail
def test_multiply_negative_numbers():
    assert False
    # calculator = Calculator(10, -10)
    # assert calculator.multiply() == -100


