import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from constant import DOMAIN_URL

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(DOMAIN_URL + '/login')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_login_correct_username_correct_password(self):
        self.driver.find_element(By.NAME, 'username').send_keys('shubham.vijayvargiya@arcgate.com')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Zxcvbn@111')
        time.sleep(2)
        self.driver.find_element(By.ID, "login_button").click()
        time.sleep(2)
        assert self.driver.current_url ==  DOMAIN_URL +'/dashboard'
        
    def test_login_correct_username_incorrect_password(self):
        self.driver.find_element(By.NAME, 'username').send_keys('shubham.vijayvargiya@arcgate.com')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Zxcvbn@11')
        time.sleep(2)
        self.driver.find_element(By.ID, "login_button").click()
        time.sleep(2)
        
    def test_login_incorrect_username_correct_password(self):
        self.driver.find_element(By.NAME, 'username').send_keys('shubham.vijayvargiya@arcgate.co')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Zxcvbn@111')
        time.sleep(2)
        self.driver.find_element(By.ID,"login_button").click()
        time.sleep(2)
        
    def test_login_incorrect_username_incorrect_password(self):
        self.driver.find_element(By.NAME, 'username').send_keys('shubham.vijayvargiya@arcgate.co')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Zxcvbn@11')
        time.sleep(2)
        self.driver.find_element(By.ID,"login_button").click()
        time.sleep(2)
        
    def test_login_blank_username_fill_password(self):
        self.driver.find_element(By.NAME, 'username').send_keys('')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Zxcvbn@111')
        time.sleep(2)
        self.driver.find_element(By.ID,"login_button").click()
        time.sleep(2)
        
    def test_login_fill_username_blank_password(self):
        self.driver.find_element(By.NAME, 'username').send_keys('shubham.vijayvargiya@arcgate.com')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('')
        time.sleep(2)
        self.driver.find_element(By.ID,"login_button").click()
        time.sleep(2)
        
    def test_login_blank_username_blank_password(self):
        self.driver.find_element(By.NAME, 'username').send_keys('')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('')
        time.sleep(2)
        self.driver.find_element(By.ID,"login_button").click()
        time.sleep(2)
                
if __name__ == '__main__':  
    unittest.main()
