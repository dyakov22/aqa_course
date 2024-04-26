import pytest
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
