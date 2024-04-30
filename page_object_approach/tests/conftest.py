import pytest
from page_object_approach import config
from page_object_approach.utils.driver_factory import driver_factory


# @pytest.fixture(scope='function')
# def driver(request):
#     driver = driver_factory(
#         request.config.get_option('--browser')
#     )
#     driver.maximize_window()
#     driver.get(config.browser.base_url)
#
#     yield driver
#
#     driver.quit()


@pytest.fixture(scope='function')
def driver(pytestconfig):
    browser = pytestconfig.getoption('browser')
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.get(config.browser.base_url)

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Help information '
    )
    # parser.addoption()