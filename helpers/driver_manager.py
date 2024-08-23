from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os

def get_driver() -> WebDriver:
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Check if running in CI/CD environment
    if os.getenv('CI') == 'true':
        options.add_argument('--headless')  # Run Chrome in headless mode in CI/CD

    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
