from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.ID,'openwindow').click()

time.sleep(10)

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,'//ul[@class="navbar-nav ml-auto"]/li[2]/a').click()
time.sleep(3)