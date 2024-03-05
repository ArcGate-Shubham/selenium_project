from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://chercher.tech/practice/implicit-wait-example')
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@id='q']/input")))
driver.find_element(By.XPATH,"//div[@id='q']/input").click()
