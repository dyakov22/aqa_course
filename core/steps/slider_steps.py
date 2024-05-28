import allure
from core.elements import slider_page
from core.helpers.soft_step import step


@allure.step('Send {value} to slider')
def send_value_to_slider_itself(value):# does not work
    slider_page.slider_value_field.send_keys(value)


@allure.step('Send {value} to slider into input')
def send_value_to_slider_input_field(value): # does not work
    slider_page.slider_value_field.send_keys(value)


@allure.step('Set {value} into slider')
def set_value_to_slider_itself(value):
    slider_page.slider_value_field.set_element_attr("value", value)


@allure.step('Set {value} into slider value field')
def set_value_to_slider_value_field(value):
    slider_page.slider_value_field.set_element_attr("value", value)


@step('This is title')
def slide_slider(**kwargs):
    slider_page.slider.slide_element()