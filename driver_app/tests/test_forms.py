
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import keys


# Create your tests here.
class SeleniumTest(LiveServerTestCase):
    
    def testHomepage(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')
        assert "Ford Dealership Driver Portal" in driver.title

class LoginFormTest(LiveServerTestCase):

    def testForm(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/accounts/login/')

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')
        submit = driver.find_element_by_id('submit')

        user_name.send_keys('admin')
        user_password.send_keys('multitude of cats')

        submit.send_keys(keys.RETURN)

        assert 'admin' in driver.page_source