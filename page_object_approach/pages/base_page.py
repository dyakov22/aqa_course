from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# MouseButton & Keys
# from selenium.webdriver import Keys
# from selenium.webdriver.common.actions.mouse_button import MouseButton

# MouseButton.LEFT
# Keys.SHIFT


class BasePage:

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    @property
    def action_chains(self):
        return ActionChains(driver=self.driver)

    # def element(self, locator, condition):
    #     condition = ec.visibility_of_element_located if not condition else condition
    #     return self.wait_until(locator, condition)

    def wait_until(self, locator: tuple, condition, **kwargs) -> WebElement:
        wait = WebDriverWait(self.driver, kwargs.get('timeout', kwargs.get("timeout", 10)))
        return wait.until(condition(locator))

    def wait_until_not(self, locator: tuple, condition, **kwargs):
        wait = WebDriverWait(self.driver, kwargs.get('timeout', kwargs.get("timeout", 10)))
        return wait.until_not(condition(locator))

    def click(self, locator: tuple):
        condition = ec.element_to_be_clickable
        element = self.wait_until(locator, condition)
        self.scroll_into_view(element).click()
        # element.click()

    def type(self, locator: tuple, value: str):
        condition = ec.visibility_of_element_located
        self.wait_until(locator, condition).send_keys(value)

    def scroll_into_view(self, element: WebElement):
        """
        Scrolling to the Top or Bottom of the Page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, 0);")

        Scrolling by a Specific Amount
        driver.execute_script("window.scrollBy(0, 100);")
        driver.execute_script("window.scrollBy(0, -100);")

        Scrolling into View with Options
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});", element)
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
