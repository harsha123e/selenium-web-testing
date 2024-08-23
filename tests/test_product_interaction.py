import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers.driver_manager import get_driver

@pytest.fixture(scope='module')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_product_selection_and_addition_to_cart(driver):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    product = driver.find_element(By.XPATH, '//div[@class="inventory_item"][1]')
    product.find_element(By.CLASS_NAME, 'btn_inventory').click()
    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == '1', "Product was not added to the cart"
