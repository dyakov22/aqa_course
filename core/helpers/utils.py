from selenium.webdriver.remote.webelement import WebElement

from core.driver.shared_driver import driver


def set_element_attr(attr: str, attr_value: str, element: WebElement):
    driver.execute_script(f"arguments[0].{attr} = {attr_value};", element)
