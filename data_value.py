import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from new_object import wait_till_text_appears

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://qavbox.github.io/demo/delay/')
driver.implicitly_wait(30)
assert 'Delay' in driver.title

# commit1 = driver.find_element(By.NAME,'commit1')
# commit1.click()

# delayEl = driver.find_element(By.ID,'delay')
# print(delayEl.text)
# time.sleep(3)


commit = driver.find_element(By.NAME,'commit')
commit.click()

el = driver.find_element(By.ID,'two')
# print("First Attempt :" + el.text)

WebDriverWait(driver, 10).until(wait_till_text_appears((By.ID ,'two'), "here!"))
print("After waiting :", el.text)
driver.quit()
        
        