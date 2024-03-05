# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://iw.arcgate.com/login')
# time.sleep(2)
# driver.find_element(By.NAME,'username').send_keys('shubham.vijayvargiya@arcgate.com')
# time.sleep(2)
# driver.find_element(By.NAME,'password').send_keys('Zxcvbn@111')
# time.sleep(2)
# driver.find_element(By.ID, "login_button").click()
# time.sleep(10)
# driver.find_element(By.XPATH,'//div[@class="container-fluid mt80"]/div[2]/div[4]/div/div/div/a[1]').click()
# time.sleep(4)
# driver.find_element(By.ID,'addButton').click()
# time.sleep(4)
# driver.find_element(By.ID,'userSettingUsername').send_keys('abhishek')
# time.sleep(3)
# driver.find_element(By.ID,'userSettingEmail').send_keys('abhishek@arcgate.com')
# time.sleep(3)
# driver.quit()


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://127.0.0.1:8000/dashboard')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element(By.NAME, 'username').send_keys('shubham.vijayvargiya@arcgate.com')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Zxcvbn@1111')
        time.sleep(2)
        self.driver.find_element(By.ID, "login_button").click()
        time.sleep(10)
        # Add assertions to verify successful login

    def test_add_user(self):
        self.driver.find_element(By.NAME, 'username').send_keys('shubham.vijayvargiya@arcgate.com')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('Zxcvbn@1111')
        time.sleep(2)
        self.driver.find_element(By.ID, "login_button").click()
        time.sleep(10)

        self.driver.find_element(By.XPATH,'//div[@class="container-fluid mt80"]/div[2]/div[4]/div/div/div/a[1]').click()
        time.sleep(4)
        self.driver.find_element(By.ID,'addButton').click()
        time.sleep(4)
        self.driver.find_element(By.ID,'userSettingUsername').send_keys('abhishek')
        time.sleep(3)
        self.driver.find_element(By.ID,'userSettingEmail').send_keys('abhishek@arcgate.com')
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//select[@id="userSettingRole"]/option[2]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//select[@id="userSettingStatus"]/option[2]').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'save-button').click()
        time.sleep(2)
        # Add assertions to verify user addition

if __name__ == '__main__':
    unittest.main()
