from selenium import webdriver

import config


def driver_factory(browser_name: str):
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": "/Users/ndiakov/PycharmProjects/aqa_courae/tests/download",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        return webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(options=options)
    else:
        return getattr(webdriver, config.browser.capitalize())()
