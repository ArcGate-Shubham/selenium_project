from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.XPATH,'//div[@class="products"]/div[1]/div[2]/a[2]').click()
driver.find_element(By.XPATH,'//div[@class="products"]/div[1]/div[3]/button').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'a.cart-icon img').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@class="cart-preview active"]/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@class="products"]/div/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//option[@value="India"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'input').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'button').click()
time.sleep(2)

time.sleep(10)
driver.quit()
