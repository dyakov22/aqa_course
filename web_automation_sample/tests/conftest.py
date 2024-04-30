import pytest
import csv

from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    implicitly_wait_value = request.node.get_closest_marker('implicitly_wait_value')
    url = request.node.get_closest_marker('url')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    if implicitly_wait_value:
        driver.implicitly_wait(time_to_wait=implicitly_wait_value.args[0])
    driver.get(url.args[0] if url else 'https://advantageonlineshopping.com/')

    yield driver

    driver.quit()


def read():
    with open('login_data.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        login_data = []
        for row in reader:
            login_data.append(row)
        return login_data


def pytest_generate_tests(metafunc):
    if 'login_data' in metafunc.fixturenames:
        values = read()
        metafunc.parametrize('login_data', values)
