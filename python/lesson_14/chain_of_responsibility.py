

class LoginPage:

    def enter_email(self, email: str):
        print(f'Entering email {email}')

    def enter_pwd(self, pwd: str):
        print(f'Entering pwd {pwd}')

    def click_on_login_btn(self):
        print('Click on the Login button')
        return HomePage()

    def should_see_title(self, title: str) -> bool:
        print('Title is checking .....')
        return title == 'Sign-in'


class HomePage:

    def should_see_title(self, title: str) -> bool:
        print('Title is checking .....')
        return title == 'Hello, John'

    def click_on_settings_btn(self):
        print('Click on the Settings button')
        return SettingsPage()


class SettingsPage:

    def click_on_sign_out(self):
        print('Click on the Sign Out button')
        return LoginPage()


def test_user_flow_to_settings():
    login_page = LoginPage()
    login_page.enter_email('asd@asd.asd')
    login_page.enter_pwd('qwe12345987654')
    home_page = login_page.click_on_login_btn()
    print(f"Is title good? {home_page.should_see_title('Hello, John')}")
    settings_page = home_page.click_on_settings_btn()
    login_page = settings_page.click_on_sign_out()
    login_page.should_see_title('asasdmklasdm')








