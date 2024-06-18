import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import time

class TestECommercePlatform(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_and_check_elements(self):
        driver = self.driver
        driver.get("https://mentordesign.company.site/?lang=en&from_admin&vertical=art")

        # Example login test
        username_input = driver.find_element(By.ID, "inputUsername")
        username_input.send_keys("mentordesign")

        password_input = driver.find_element(By.ID, "inputPassword")
        password_input.send_keys("your_password_here")
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)  # wait for page to load

        # Verify that the login was successful by checking the presence of a specific element
        self.assertIn("Dashboard", driver.title, "Login failed or dashboard not loaded")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
