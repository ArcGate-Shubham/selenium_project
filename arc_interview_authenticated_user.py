import unittest
import time
from arc_interview_login import TestLoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from constant import DOMAIN_URL

class AutenticatedUser(TestLoginPage,unittest.TestCase):
    
        def setUp(self):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get(DOMAIN_URL + '/login')
            time.sleep(2)
            
        def tearDown(self):
            self.driver.quit()

        def test_authenticated_user_correct_detail(self):
            self.test_login_correct_username_correct_password()
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//div[@class="container-fluid mt80"]/div[2]/div[4]/div/div/div/a[1]').click()
            self.driver.find_element(By.ID,'addButton').click()
            time.sleep(2)
            self.driver.find_element(By.ID,'userSettingUsername').send_keys('tarun')
            time.sleep(2)
            self.driver.find_element(By.ID,'userSettingEmail').send_keys('tarun@arcgate.com')
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//select[@id="userSettingRole"]/option[2]').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//select[@id="userSettingStatus"]/option[3]').click()
            time.sleep(2)
            self.driver.find_element(By.ID,'save-button').submit()
            time.sleep(2)
            
if __name__ == '__main__':  
    unittest.main()