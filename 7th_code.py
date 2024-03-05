import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/upload')
driver.find_element(By.ID,'file-upload').send_keys('/home/arcgate/college-data.jpeg')
time.sleep(2)
driver.find_element(By.ID,'file-submit').click()
time.sleep(2)
driver.quit()