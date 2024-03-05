from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.XPATH,"//a[contains(text(),'Top')]")).click().perform()

time.sleep(3)
driver.quit()