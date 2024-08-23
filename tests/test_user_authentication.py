import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.driver_manager import get_driver

@pytest.fixture(scope='module')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize('username, password, expected_message', [
    ('standard_user', 'secret_sauce', 'Products'),
    ('invalid_user', 'invalid_password', 'Epic sadface:')
])
def test_login(driver, username, password, expected_message):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

    if username == 'standard_user':
        welcome_message = driver.find_element(By.CLASS_NAME, 'title').text
        assert welcome_message == expected_message, "Login failed or welcome message not found"
    else:
        error_message = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
        assert expected_message in error_message, "Error message not found or incorrect"

def test_logout(driver):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))).click()
    login_button = driver.find_element(By.ID, 'login-button')
    assert login_button.is_displayed(), "Logout failed or login button not found"
