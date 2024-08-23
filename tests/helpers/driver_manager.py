import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver():
    browser = os.getenv('BROWSER', 'chrome')  # Default to Chrome if not set

    if browser == 'chrome':
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError("Unsupported browser: " + browser)
