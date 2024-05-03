from selenium.webdriver.remote import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from core.driver import shared_driver
from core.helpers.locator import by


class Element:

    def __init__(self, locator: tuple, driver=lambda: shared_driver.driver):
        self.locator = locator
        self._driver = driver if callable(driver) else lambda : driver

    @property
    def driver(self) -> webdriver:
        return self._driver()

    def wait_until(self, locator: tuple, condition, **kwargs) -> WebElement:
        wait = WebDriverWait(self.driver, kwargs.get('timeout', kwargs.get("timeout", 10)))
        return wait.until(condition(locator))

    def wait_until_not(self, locator: tuple, condition, **kwargs):
        wait = WebDriverWait(self.driver, kwargs.get('timeout', kwargs.get("timeout", 10)))
        return wait.until_not(condition(locator))

    def click(self, **kwargs):
        self.wait_until(self.locator, ec.element_to_be_clickable, **kwargs).click()

    def is_displayed(self, **kwargs):
        return self.wait_until(self.locator, ec.visibility_of_element_located, **kwargs).is_displayed()


def element(locator: str):
    return Element(by(locator))

