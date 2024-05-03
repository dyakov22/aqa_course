import pytest

from core.steps import alerts_frames_steps


@pytest.mark.route('alerts')
def test_simple_alert():
    alerts_frames_steps.click_on_left_side_menu_alert_btn()
    alerts_frames_steps.click_on_simple_alert_btn()