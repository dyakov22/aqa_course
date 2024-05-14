from core.helpers.element import element

progress_bar = element(locator='css=[role="progressbar"]')

progress_bar_variant_dima = lambda value: element(locator=f"css=[aria-valuenow='{value}']")

start_stop_btn = element(locator="id=startStopButton")
