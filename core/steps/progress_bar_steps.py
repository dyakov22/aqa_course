from core.elements import progress_bar


def wait_until_progress_bar_has_attr_value(value: str):
    progress_bar.progress_bar.wait_until_attr_has_value(attr="aria-valuenow", value=value)


def wait_until_progress_bar_has_attr_value_variant_2(value: str):
    progress_bar.progress_bar_variant_dima(value=value).is_displayed()


def click_start_stop_btn():
    progress_bar.start_stop_btn.click()
