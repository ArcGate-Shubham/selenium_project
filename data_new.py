import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# def test_sample1():
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get('https://qavbox.github.io/demo/signup/')
time.sleep(3)
assert 'Registration' in driver.title



# action = ActionChains(driver)
# driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
# time.sleep(3)
# right_click_element = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
# action.context_click(right_click_element).send_keys(Keys.ARROW_DOWN).pause(2)\
#     .send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ENTER).perform()
# time.sleep(3)
# driver.quit()



action = ActionChains(driver)
username = driver.find_element(By.ID,'username')
email = driver.find_element(By.ID,'email')
username.send_keys('QAVBOX')
action.key_down(Keys.COMMAND).key_down("A").key_up(Keys.COMMAND).perform()
time.sleep(2)
action.key_down(Keys.COMMAND).key_down("C").key_up(Keys.COMMAND).perform()
time.sleep(3)
action.click(email).key_down(Keys.COMMAND).key_down("V").key_up(Keys.COMMAND).perform()
time.sleep(4)
driver.quit()