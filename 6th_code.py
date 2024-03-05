import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.XPATH,'//input[@id="name"]').send_keys('vijay')
driver.find_element(By.CSS_SELECTOR,'input#confirmbtn').click()
popup_data = driver.switch_to.alert
time.sleep(2)

assert "vijay" in popup_data.text
popup_data.dismiss()
time.sleep(3)
driver.quit()