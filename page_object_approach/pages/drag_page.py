from selenium.webdriver.remote.webdriver import WebDriver

from page_object_approach.pages.base_page import BasePage
from page_object_approach.utils.by import by
from selenium.webdriver.support import expected_conditions as ec


class DragPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.drag_box = by('id=dragBox')
        self.cursor_btn = by('id=draggableExample-tab-cursorStyle')

    # def click_on_drag_box(self):
    #     self.click(drag_locators.drag_box)

    def click_on_drag_box(self):
        self.click(self.drag_box)

    def drag_and_drop_drag_box(self):
        source = self.wait_until(self.drag_box, ec.presence_of_element_located)
        target = self.wait_until(self.cursor_btn, ec.visibility_of_element_located)
        self.action_chains.drag_and_drop(source=source, target=target).perform()
