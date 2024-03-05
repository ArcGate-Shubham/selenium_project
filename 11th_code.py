from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/#top')
data = driver.find_element(By.ID,'name')
data.send_keys('anshul')
ineer = data.get_attribute('value')
print(ineer)