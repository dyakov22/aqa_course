from selenium.webdriver.remote.webdriver import WebDriver

from page_object_approach.pages.base_page import BasePage
from page_object_approach.pages.drag_page import DragPage
from page_object_approach.utils.by import by


class HomePage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.interactions_btn = by('contain_text=Interactions')
        self.drag_btn = by('contain_text=Dragabble')

    def click_on_interactions_btn(self):
        self.click(self.interactions_btn)
        return self

    def click_on_draggable_btn(self) -> DragPage:
        self.click(self.drag_btn)
        return DragPage(self.driver)
