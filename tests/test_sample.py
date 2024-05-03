import pytest

from core.steps import home_steps


def test_sample():
    home_steps.click_on_elements_block()


# def test_(driver):
#     home_page = HomePage(driver)
#     home_page.click_on_elements()
#
# @pytest.mark.page_name('HomePage')
# def test_(page):
#     page.click_on_elements()
