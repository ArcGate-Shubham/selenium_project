import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.neuralnine.com/")
driver.implicitly_wait(5)


links = driver.find_elements(By.XPATH,"//a[@href]")
for link in links:
   if 'Books' in link.get_attribute('innerHTML'):
       link.click()
       break
   
time.sleep(5)

book_links = driver.find_elements("xpath","//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")
time.sleep(2)
book_links[0].click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(4)
buttons = driver.find_elements("xpath","//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")
time.sleep(5)
for button in buttons:
    print(button.get_attribute("innerHTML"))
time.sleep(10)

