import pytest

from core.steps import upload_download_steps
from tests.test_data import choose_file


@pytest.mark.route('upload-download')
@pytest.mark.regression
@pytest.mark.parametrize("file_type", ["txt", "csv"])
def test_file_name_appearance_after_file_uploading(file_type):
    file = choose_file(file_type)
    upload_download_steps.upload_file(file_path=file)
    upload_download_steps.file_name_is_displayed(value=rf"C:\fakepath\{file.split('/')[-1]}")


@pytest.mark.route('upload-download')
@pytest.mark.regression
def test_download_file():
    upload_download_steps.click_on_download_file_btn()