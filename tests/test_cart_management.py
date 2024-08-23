import pytest
from selenium.webdriver.common.by import By
from helpers.driver_manager import get_driver

@pytest.fixture(scope='module')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_adding_multiple_products_to_cart(driver):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    products = driver.find_elements(By.CLASS_NAME, 'btn_inventory')
    for product in products:
        product.click()
    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == str(len(products)), "Not all products were added to the cart"

def test_removing_products_from_cart(driver):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Add a product to the cart
    driver.find_element(By.CLASS_NAME, 'btn_inventory').click()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    
    # Capture the initial number of items in the cart
    initial_cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    initial_count = int(initial_cart_badge) if initial_cart_badge else 0
    
    # Remove the product from the cart
    driver.find_element(By.CLASS_NAME, 'btn_secondary').click()
    
    # Verify that the cart badge number decreased by one
    updated_cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    updated_count = int(updated_cart_badge) if updated_cart_badge else 0
    
    assert updated_count == initial_count - 1, "Cart badge number did not decrease by one after removing a product."


