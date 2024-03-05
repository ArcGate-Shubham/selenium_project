import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.cleartrip.com/do/search/fligths")
driver.find_element(By.NAME,'from').send_keys('del')
time.sleep(2)
from_airport = driver.find_elements(By.XPATH,'//ul[@id="ui-id-1"]/li/div')
for airport in from_airport:
    if airport.text == "Adelaide, AU - Adelaide (ADL)":
        airport.click()
    else:
        pass

time.sleep(2)
driver.quit()