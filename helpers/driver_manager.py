import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver():
    browser = os.getenv('BROWSER', 'chrome')
    headless = os.getenv('HEADLESS', 'False').lower() == 'true'

    options = Options()
    options.headless = headless  # Set headless mode based on environment variable

    if browser == 'chrome':
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = headless
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    else:
        raise ValueError("Unsupported browser: " + browser)
