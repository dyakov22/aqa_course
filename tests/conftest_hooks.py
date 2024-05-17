import pytest


@pytest.fixture(autouse=True)
def fixture_2():
    print('Fixture is FIX 2')