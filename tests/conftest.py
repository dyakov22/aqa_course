import allure
import pytest

import config
from core.driver import shared_driver
from core.helpers.driver_factory import driver_factory
from core.helpers.soft_step import ErrCatcher

pytest_plugins = [
    'tests.conftest_hooks',
    'tests_api.conftest'
]

def pytest_html_report_title(report):
    report.title = "My very own title!"


@allure.title("Prepare driver for the test")
@pytest.fixture(scope='function', autouse=True)
def driver(request, pytestconfig):
    url = config.browser.base_url
    if request.node.get_closest_marker('route'):
        url += request.node.get_closest_marker('route').args[0]

    driver = driver_factory(config.browser.type, test_case_name=request.node.name)

    shared_driver.driver = driver
    driver.maximize_window()
    driver.get(url)

    yield driver

    driver.quit()



def pytest_exception_interact(node, call, report):
    try:
        allure.attach(shared_driver.driver.get_screenshot_as_png(), 'Screenshot for demostrate',
                      attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(e)


@pytest.fixture(name='catcher')
def assertion_catcher():
    return ErrCatcher()

