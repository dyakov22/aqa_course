import pytest

from core.steps import progress_bar_steps


@pytest.mark.route("progress-bar")
def test_wait_for_attr_to_be():
    progress_bar_steps.click_start_stop_btn()
    progress_bar_steps.wait_until_progress_bar_has_attr_value("50")
    progress_bar_steps.click_start_stop_btn()


@pytest.mark.route("progress-bar")
@pytest.mark.parametrize('index', range(4))
def test_wait_for_attr_to_be_variant_2(index):
    progress_bar_steps.click_start_stop_btn()
    progress_bar_steps.wait_until_progress_bar_has_attr_value_variant_2("10")
    progress_bar_steps.click_start_stop_btn()
