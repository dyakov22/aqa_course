from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from core.driver.shared_driver import driver


def scroll_into_view(element: WebElement):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    return element


def get_cookie(name: str):
    driver.get_cookie(name=name)


def delete_cookies(name: str = None, is_all: bool = False):
    if name:
        driver.delete_cookie(name=name)
    elif is_all:
        driver.delete_all_cookies()


def add_cookie(name: str, value: str):
    driver.add_cookie({"name": name, "value": value})


def set_local_storage_value(name: str, value: str):
    driver.execute_script(f"window.localStorage.setItem('{name}', '{value})")


def get_local_storage_value(name: str):
    return driver.execute_script(f"return window.localStorage.getItem('{name}')")


def delete_local_storage_value(name: str):
    driver.execute_script(f"window.localStorage.removeItem('{name}')")


def wait_for_alert(timeout: int = 10):
    wait = WebDriverWait(driver=driver, timeout=timeout)
    return wait.until(ec.alert_is_present)


def accept_alert():
    wait_for_alert().accept()


def dismiss_alert():
    wait_for_alert().dismiss()


def alert_has_text(text: str):
    assert wait_for_alert().text == text
