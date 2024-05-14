from selenium.webdriver import ActionChains
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

    def action_chains(self):
        return ActionChains(self.driver)

    def wait_until(self, locator: tuple, condition, **kwargs) -> WebElement:
        timeout = kwargs.pop("timeout", 10)
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.1)
        return wait.until(condition(locator, **kwargs))

    def wait_until_not(self, locator: tuple, condition, **kwargs):
        timeout = kwargs.pop("timeout", 10)
        wait = WebDriverWait(self.driver, timeout)
        return wait.until_not(condition(locator))

    def send_keys(self, value: str, **kwargs):
        self.wait_until(self.locator, ec.visibility_of_element_located, **kwargs).send_keys(value)

    def element_has_text(self, value: str, **kwargs):
        actual_text = self.wait_until(self.locator, ec.visibility_of_element_located, **kwargs).text
        assert actual_text == value, f"Expect {value} text, actual: {actual_text}"

    def click(self, **kwargs):
        self.wait_until(self.locator, ec.element_to_be_clickable, **kwargs).click()

    def is_displayed(self, **kwargs):
        return self.wait_until(self.locator, ec.visibility_of_element_located, **kwargs).is_displayed()

    def wait_until_attr_has_value(self, attr: str, value: str):
        self.wait_until(locator=self.locator, condition=ec.text_to_be_present_in_element_attribute,
                        attribute_=attr, text_=value)

    def set_element_attr(self, attr: str, attr_value: str):
        el = self.wait_until(self.locator, ec.visibility_of_element_located)
        shared_driver.driver.execute_script(f"arguments[0].{attr} = {attr_value};", el)

    def slide_element(self):
        el = self.wait_until(self.locator, ec.visibility_of_element_located)

        width = el.size["width"]

        # self.action_chains().click_and_hold(el).move_by_offset(width / 3, 0).release().perform()

        # could combine both variants

        # self.action_chains().move_to_element_with_offset(el, 20, 20).click().perform()

        target_percentage = 75
        offset = (width * target_percentage / 100) - (width / 2)
        self.action_chains().click_and_hold(el).move_by_offset(offset, 0).release().perform()


def element(locator: str):
    return Element(by(locator))

