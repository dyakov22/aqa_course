import pytest

from core.elements import advantage_qa
from lessons.db.context_manager import read_from_db


@pytest.mark.parametrize('username, password', read_from_db('testing_data.db'))
def test_db(username, password):
    advantage_qa.init_sign_in_process_btn.click()
    advantage_qa.sign_in_username_field.send_keys(username)
    advantage_qa.sign_in_password_field.send_keys(password)
    advantage_qa.sign_in_btn.click()
    advantage_qa.sign_in_msg.element_has_text('Incorrect user name or password.')