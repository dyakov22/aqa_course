from core.elements import upload_download_page


def upload_file(file_path: str):
    upload_download_page.upload_file_input.send_keys(value=file_path)


def file_name_is_displayed(value: str):
    upload_download_page.uploaded_file_label.element_has_text(value=value)


def click_on_download_file_btn():
    upload_download_page.download_file_btn.click()
