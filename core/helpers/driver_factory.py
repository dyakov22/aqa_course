from selenium import webdriver

import config


def driver_factory(browser_name: str, test_case_name: str):
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.browser_version = 'latest'
        options.platform_name = 'Windows 11'
        sauce_options = {}
        sauce_options['username'] = 'oauth-plink.sign0-335ba'
        sauce_options['accessKey'] = '58c34b4c-fc64-43b4-809d-980240b9b672'
        sauce_options['build'] = 'selenium-build-HWDKE'
        sauce_options['name'] = test_case_name
        options.set_capability('sauce:options', sauce_options)
        return webdriver.Remote(command_executor="https://ondemand.eu-central-1.saucelabs.com:443/wd/hub",
                                options=options)

    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(options=options)
    else:
        return getattr(webdriver, config.browser.capitalize())()


# def driver_factory_lambda_test(browser_name: str, test_case_name: str):
#     username =
#     access_key =
#
#     selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
#     chrome_options = webdriver.ChromeOptions()
#     option = {
#         "platform": "Windows 10",
#         "version": "latest",
#         "name": test_case_name,
#         "Build": build,
#         "video": True,
#         "visual": True,
#         "network": True,
#         "console": True
#     }
#     chrome_options.set_capability("LT:Options", option)
#     return webdriver.Remote(
#         command_executor=selenium_endpoint,
#         options=chrome_options
#     )