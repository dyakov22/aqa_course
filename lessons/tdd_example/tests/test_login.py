import pytest

from lessons.tdd_example.tests.helpers import read


def test_login_with_pytest_generate_tests(login_data):
    assert 1 == login_data


@pytest.mark.parametrize('login_values', read())
def test_login_with_parametrize(login_values):
    assert 1 == login_values





# Example without pytest generate tests and using func in parametrize


# login_values = [(1,2,3), (4,5,6)]
# login_key = 'login_values'
#
#
# @pytest.mark.parametrize(login_key, login_values)
# def test_login_with_parametrize(login_values):
#     assert 1 == login_values
#
#
# @pytest.mark.parametrize(login_key, login_values)
# def test_login_with_parametrize_second(login_values):
#     assert 2 == login_values