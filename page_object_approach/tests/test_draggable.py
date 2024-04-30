import pytest

from page_object_approach.pages.home_page import HomePage


def test_open_draggable_page(driver):
    home_page = HomePage(driver)
    home_page.click_on_interactions_btn()
    drag_page = home_page.click_on_draggable_btn()
    drag_page.drag_and_drop_drag_box()


@pytest.mark.skip('Not actual')
def test_open_draggable_page_with_self(driver):
    home_page = HomePage(driver)
    drag_page = (home_page.click_on_interactions_btn().
                 click_on_draggable_btn())
    drag_page.click_on_drag_box()
