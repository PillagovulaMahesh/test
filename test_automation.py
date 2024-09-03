from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class ECommerceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')  # Run headless mode
        cls.driver = webdriver.Chrome(service=Service('path/to/chromedriver'), options=options)
        cls.driver.get('http://automationpractice.com/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_and_add_to_cart(self):
        driver = self.driver
        search_box = driver.find_element(By.ID, 'search_query_top')
        search_box.send_keys('Dress')
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        product = driver.find_element(By.CSS_SELECTOR, '.product_list .product-container')
        product.click()

        add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '.exclusive')
        add_to_cart_button.click()
        time.sleep(2)

        proceed_to_checkout_button = driver.find_element(By.CSS_SELECTOR, '.button-medium')
        proceed_to_checkout_button.click()
        time.sleep(2)

        # Validate the product is added to the cart
        cart_product = driver.find_element(By.CSS_SELECTOR, '.cart_description')
        self.assertTrue(cart_product.is_displayed(), 'Product was not added to the cart.')

        # Proceed through checkout process (additional steps might be required)

    def test_login(self):
        driver = self.driver
        sign_in_button = driver.find_element(By.CLASS_NAME, 'login')
        sign_in_button.click()
        time.sleep(2)

        email_field = driver.find_element(By.ID, 'email')
        password_field = driver.find_element(By.ID, 'passwd')
        submit_button = driver.find_element(By.ID, 'SubmitLogin')

        email_field.send_keys('valid.email@example.com')
        password_field.send_keys('validpassword')
        submit_button.click()
        time.sleep(2)

        # Validate successful login
        account_name = driver.find_element(By.CSS_SELECTOR, '.account')
        self.assertTrue(account_name.is_displayed(), 'Login failed or user is not logged in.')

    def test_ui_elements(self):
        driver = self.driver
        search_box = driver.find_element(By.ID, 'search_query_top')
        self.assertTrue(search_box.is_displayed(), 'Search box is not displayed.')

        nav_menu = driver.find_element(By.CSS_SELECTOR, '.sf-menu')
        self.assertTrue(nav_menu.is_displayed(), 'Navigation menu is not displayed.')

        footer = driver.find_element(By.ID, 'footer')
        self.assertTrue(footer.is_displayed(), 'Footer is not displayed.')

    def test_form_validation(self):
        driver = self.driver
        contact_button = driver.find_element(By.LINK_TEXT, 'Contact us')
        contact_button.click()
        time.sleep(2)

        email_field = driver.find_element(By.ID, 'email')
        message_field = driver.find_element(By.ID, 'message')
        send_button = driver.find_element(By.ID, 'submitMessage')

        email_field.send_keys('invalid email')
        message_field.send_keys('')
        send_button.click()
        time.sleep(2)

        # Validate error messages
        email_error = driver.find_element(By.CSS_SELECTOR, '.form-error')
        self.assertTrue(email_error.is_displayed(), 'Email error message not displayed.')

        message_error = driver.find_element(By.CSS_SELECTOR, '.form-error')
        self.assertTrue(message_error.is_displayed(), 'Message error message not displayed.')

if __name__ == '__main__':
    import unittest
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
