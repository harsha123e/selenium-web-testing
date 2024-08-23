import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.driver_manager import get_driver
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserAuthenticationTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # Refresh browser state before each test.
        self.driver.get('https://www.saucedemo.com')  # Navigate to the starting page

    def test_login_valid(self):
        driver = self.driver
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        
        # Add assertions to verify login success
        welcome_message = driver.find_element(By.CLASS_NAME, 'title').text
        self.assertEqual(welcome_message, 'Products', "Login failed or welcome message not found")

        logger.info("Completed test_login_valid")

    def test_login_invalid(self):
        driver = self.driver
        driver.find_element(By.ID, 'user-name').send_keys('invalid_user')
        driver.find_element(By.ID, 'password').send_keys('invalid_password')
        driver.find_element(By.ID, 'login-button').click()
        
        # Add assertions to verify login failure
        error_message = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
        self.assertIn("Epic sadface:", error_message, "Error message not found or incorrect")

        logger.info("Completed test_login_invalid")

    def test_logout(self):
        driver = self.driver
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        
        # Perform logout
        driver.find_element(By.ID, 'react-burger-menu-btn').click()
        
        # Wait for the logout link to be clickable and then click
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))).click()
        
        # Add assertions to verify successful logout
        login_button = driver.find_element(By.ID, 'login-button')
        self.assertTrue(login_button.is_displayed(), "Logout failed or login button not found")
        logger.info("Completed test_logout")


if __name__ == "__main__":
    unittest.main()
