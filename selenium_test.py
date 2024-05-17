import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import multiprocessing
import time
from unittest import TestCase
from app import app, db
from app.config import TestConfig

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome Driver
        self.driver = webdriver.Chrome()

    def test_home_page(self):
        driver = self.driver
        driver.get("http://localhost:5000")  # URL to your app
        self.assertIn("HTML", driver.title)  # Check the title in the Home page

    def test_login_functionality(self):
        driver = self.driver
        driver.get("http://localhost:5000/login")
        
        # Assuming you have 'username' and 'password' fields in your login form
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.ID, 'login-button')
        
        username_field.send_keys("testuser")
        password_field.send_keys("testpass")
        login_button.click()

        # Check for a sign of successful login
        welcome_message = driver.find_element(By.ID, 'welcome-message').text
        self.assertIn("Welcome", welcome_message)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
