
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Create your tests here.
class SeleniumTest(LiveServerTestCase):
    
    def testHomepage(self):
        driver = webdriver.Chrome()

        driver.get('http://localhost:8000/')
        assert "Ford Dealership Driver Portal" in driver.title

class LoginFormTest(LiveServerTestCase):

    def testForm(self):
        driver = webdriver.Chrome()

        driver.get('http://localhost:8000/accounts/login/')

        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.NAME, 'password')
        submit = driver.find_element(By.NAME, 'submitBtn')

        user_name.send_keys('admin')
        user_password.send_keys('multitude of cats')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source