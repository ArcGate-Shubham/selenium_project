from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# driver.find_element(By.CSS_SELECTOR,'input[value="radio1"]').click()

# driver.find_element(By.XPATH,'//input[@value="radio1"]').click()

# data = driver.find_element(By.XPATH,'//legend[text()="Checkbox Example"]').text
# print(data)

# value = driver.find_element(By.XPATH,'//select[@id="dropdown-class-example"]/option[2]').text
# print(value)

# dataset = driver.find_element(By.XPATH,'//select[@id="dropdown-class-example"]/option[last()]').text
# print(dataset)

# dataValue = driver.find_element(By.XPATH,'//div[@class="tableFixHead"]/table/tbody/tr[5]/td[2]').text
# print(dataValue)

# demo = driver.find_element(By.XPATH,'//option[@value="option3"]/ancestor::div[@class="block large-row-spacer"]')

# driver.find_element(By.XPATH,'//option[starts-with(@value,"option")]').click()


# checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
# for checkbox in checkboxes:
#     if checkbox == checkboxes[1]:
#         pass
#     else:
#         checkbox.click()
        
        
time.sleep(10)
driver.quit()
