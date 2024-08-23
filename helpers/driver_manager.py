import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver():
    browser = os.getenv('BROWSER', 'chrome')

    if browser == 'chrome':
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ChromeOptions())
    
    elif browser == 'firefox':
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=FirefoxOptions())
    
    else:
        raise ValueError(f"Unsupported browser: {browser}")
