from core.elements import slider_page


def send_value_to_slider_itself(value):# does not work
    slider_page.slider_value_field.send_keys(value)


def send_value_to_slider_input_field(value): # does not work
    slider_page.slider_value_field.send_keys(value)


def set_value_to_slider_itself(value):
    slider_page.slider_page.set_element_attr("value", value)


def set_value_to_slider_value_field(value):
    slider_page.slider_value_field.set_element_attr("value", value)


def slide_slider():
    slider_page.slider.slide_element()