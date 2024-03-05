from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.switch_to.frame(driver.find_element(By.ID,'courses-iframe'))
driver.find_element(By.XPATH,'//div[@class="nav-outer clearfix"]//a[normalize-space()="Job Support"]').click()
time.sleep(10)
driver.switch_to.default_content()
driver.find_element(By.ID,'checkBoxOption1').click()
time.sleep(5)