import pytest

from tdd_example.tests.helpers import read


@pytest.fixture(params=read())
def data_from_file(request):
    return request.param


@pytest.fixture(scope='class')
def data_from_file_with_scope_class(request):
    request.cls.test_data = read()


def pytest_generate_tests(metafunc):
    if 'login_data' in metafunc.fixturenames:
        values = read()
        metafunc.parametrize('login_data', values)













