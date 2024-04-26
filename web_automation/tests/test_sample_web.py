import time
from typing import Union

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from web_automation.config_parser import config


# def test_with_webdriver_manager():
#     pip install webdriver-manager
#     from selenium.webdriver.chrome.service import Service as ChromeService
#     from webdriver_manager.chrome import ChromeDriverManager
#     service = ChromeService(ChromeDriverManager(driver_version='114.0.5735.16').install())
#     driver = webdriver.Chrome(service=service)
#     time.sleep(60)

@pytest.mark.implicitly_wait_value(10)
def test_sample_web_with_implicitly_wait(driver):

    # driver.find_element(by=By.ID, value="menuUserLink").click()

    element = driver.find_element(by=By.ID, value="menuUserLink")
    element.click()

    pop_up = driver.find_element(by=By.CSS_SELECTOR, value='.PopUp')
    assert pop_up.is_displayed()

    sign_in_btn = driver.find_element(value='sign_in_btn')
    assert not sign_in_btn.is_enabled()  # Expect False from is_enable()

    username_input = driver.find_element(by=By.NAME, value='username')
    username_input.clear()
    username_input.send_keys('aqa_course')

    pwd_input = driver.find_element(by='xpath',    #By.XPATH,
                                    value="//div[@class='inputContainer ng-scope']/child::input[@type='password']")
    pwd_input.clear()
    pwd_input.send_keys('Looxas134')

    assert sign_in_btn.is_enabled()
    sign_in_btn.click()

    signed_in_icon = driver.find_element(by=By.LINK_TEXT, value='aqa_course')
    assert signed_in_icon.is_displayed()


def wait_until(driver, locator: Union[tuple, WebElement], condition, **kwargs):
    wait = WebDriverWait(driver=driver, timeout=kwargs.get('timeout', 5))
    return wait.until(condition(locator))


def test_sample_web_explicit_wait(driver):
    wait_until(driver, (By.ID, 'menuUserLink'), ec.element_to_be_clickable).click()
    wait_until(driver, (By.CSS_SELECTOR, '.PopUp'), ec.visibility_of_element_located)
    sign_in_btn = wait_until(driver, (By.ID, 'sign_in_btn'), ec.visibility_of_element_located)
    assert not sign_in_btn.is_enabled()  # Expect False from is_enable()
    username_input = wait_until(driver, (By.NAME, 'username'), ec.visibility_of_element_located)
    username_input.clear()
    username_input.send_keys('aqa_course')
    time.sleep(3)
    pwd_input = wait_until(driver, (By.XPATH,
                                         "//div[@class='inputContainer ng-scope']/child::input[@type='password']"), ec.visibility_of_element_located)
    pwd_input.clear()
    pwd_input.send_keys('Looxas134')
    assert sign_in_btn.is_enabled()
    wait_until(driver, sign_in_btn, ec.element_to_be_clickable, timeout=15).click()
    wait_until(driver, (By.LINK_TEXT, 'aqa_course'), ec.visibility_of_element_located)


def test_sample_web_explicit_wait_with_config(driver):
    wait_until(driver, (By.ID, 'menuUserLink'), ec.element_to_be_clickable).click()
    wait_until(driver, (By.CSS_SELECTOR, '.PopUp'), ec.visibility_of_element_located)
    sign_in_btn = wait_until(driver, (By.ID, 'sign_in_btn'), ec.visibility_of_element_located)
    assert not sign_in_btn.is_enabled()  # Expect False from is_enable()
    username_input = wait_until(driver, (By.NAME, 'username'), ec.visibility_of_element_located)
    username_input.clear()
    username_input.send_keys(config.get('user', 'username'))
    time.sleep(3)
    pwd_input = wait_until(driver, (By.XPATH,
                                         "//div[@class='inputContainer ng-scope']/child::input[@type='password']"), ec.visibility_of_element_located)
    pwd_input.clear()
    pwd_input.send_keys(config.get('user', 'password'))
    assert sign_in_btn.is_enabled()
    wait_until(driver, sign_in_btn, ec.element_to_be_clickable, timeout=15).click()
    wait_until(driver, (By.LINK_TEXT, 'aqa_course'), ec.visibility_of_element_located)


@pytest.mark.url("https://demoqa.com/dynamic-properties")
def test_sample_web_qa_demo(driver):
    wait_until(driver, (By.ID, 'enableAfter'), ec.element_to_be_clickable, timeout=10)
    assert wait_until(driver, (By.ID, 'visibleAfter'), ec.visibility_of_element_located, timeout=10).is_displayed()


@pytest.mark.url(config.get('website', 'qa_demo_url') + "dynamic-properties")
def test_sample_web_qa_demo_with_config(driver):
    wait_until(driver, (By.ID, 'enableAfter'), ec.element_to_be_clickable, timeout=10)
    assert wait_until(driver, (By.ID, 'visibleAfter'), ec.visibility_of_element_located, timeout=10).is_displayed()


# Try to avoid this approach
@pytest.mark.url("https://demoqa.com/dynamic-properties")
@pytest.mark.implicitly_wait_value(1)
def test_sample_web_qa_demo(driver):
    driver.find_element(By.CSS_SELECTOR, '[id="visibleAfter"]')









