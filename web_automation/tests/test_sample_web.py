import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# def test_with_webdriver_manager():
#     pip install webdriver-manager
#     from selenium.webdriver.chrome.service import Service as ChromeService
#     from webdriver_manager.chrome import ChromeDriverManager
#     service = ChromeService(ChromeDriverManager(driver_version='114.0.5735.16').install())
#     driver = webdriver.Chrome(service=service)
#     time.sleep(60)



def test_sample_web():
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(time_to_wait=8)
    """Sets a sticky timeout to implicitly wait for an element to be found,
            or a command to complete. This method only needs to be called one time
            per session. To set the timeout for calls to execute_async_script, see
            set_script_timeout.
    """

    driver.get('https://advantageonlineshopping.com/')

    # driver.find_element(by=By.ID, value="menuUserLink").click()

    element = driver.find_element(by=By.ID, value="menuUserLink")
    element.click()

    pop_up = driver.find_element(by=By.CSS_SELECTOR, value='.PopUp')
    assert pop_up.is_displayed()

    sign_in_btn = driver.find_element(value='sign_in_btn')
    assert not sign_in_btn.is_enabled()  # Expect False from is_enable()

    username_input = driver.find_element(by=By.NAME, value='username')
    username_input.clear()
    username_input.send_keys('aqa_course')

    pwd_input = driver.find_element(by='xpath',    #By.XPATH,
                                    value="//div[@class='inputContainer ng-scope']/child::input[@type='password']")
    pwd_input.clear()
    pwd_input.send_keys('Looxas134')

    assert sign_in_btn.is_enabled()
    sign_in_btn.click()

    signed_in_icon = driver.find_element(by=By.LINK_TEXT, value='aqa_course')
    assert signed_in_icon.is_displayed()

    driver.quit()
