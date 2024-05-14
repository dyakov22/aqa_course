import pytest
from core.steps import slider_steps


@pytest.mark.route('slider')
@pytest.mark.skip('Does not work')
def test_send_value_via_attr_to_slider(): # does not work
    slider_steps.send_value_to_slider_itself("20")
    slider_steps.send_value_to_slider_input_field("30")


@pytest.mark.route('slider')
def test_set_slider_value_via_attr():
    slider_steps.set_value_to_slider_itself("20")
    slider_steps.set_value_to_slider_value_field("30")


@pytest.mark.route('slider')
def test_set_slider_value_via_action_chains():
    slider_steps.slide_slider()
