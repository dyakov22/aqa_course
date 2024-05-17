import pytest

import config
from core.driver import shared_driver
from core.helpers.driver_factory import driver_factory


pytest_plugins = [
    'tests.conftest_hooks'
]


@pytest.fixture(scope='function', autouse=True)
def driver(request, pytestconfig):
    url = config.browser.base_url
    if request.node.get_closest_marker('route'):
        url += request.node.get_closest_marker('route').args[0]

    driver = driver_factory('chrome')

    shared_driver.driver = driver
    driver.maximize_window()
    driver.get(url)

    yield driver

    driver.quit()





#
# @pytest.fixture
# def page(driver, request):
#     page_name =request.node.get_closest_marker('page_name').args[0]
#     return eval(page_name)(driver)