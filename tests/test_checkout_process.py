import pytest
from selenium.webdriver.common.by import By
from helpers.driver_manager import get_driver

@pytest.fixture(scope='module')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_complete_purchase(driver):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.CLASS_NAME, 'btn_inventory').click()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    driver.find_element(By.ID, 'checkout').click()

    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()

    driver.find_element(By.ID, 'finish').click()

    confirmation_message = driver.find_element(By.CLASS_NAME, 'complete-header').text
    assert "thank you for your order" in confirmation_message.lower(), "Order was not completed successfully"
