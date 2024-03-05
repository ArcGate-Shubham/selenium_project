# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()

# # Open Gmail
# driver.get('https://www.gmail.com')

# # Find the email input field and enter your email address
# email_input = driver.find_element(By.NAME,'identifier')
# email_input.send_keys('')
# email_input.send_keys(Keys.RETURN)
# # time.sleep(60)

# # Wait for a while to let the page load
# time.sleep(2)

# # Find the password input field and enter your password
# password_input = driver.find_element(By.NAME,'Passwd')
# password_input.send_keys('Zxcvbn@111')
# password_input.send_keys(Keys.RETURN)
# time.sleep(5)

# # You are now logged in to your Gmail account

# # Do your automation tasks here, e.g., send an email, read emails, etc.

# # Close the browser
# driver.quit()

# import os
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google_auth_oauthlib.flow import Flow
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService

# # Set up the OAuth 2.0 flow
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
# flow = InstalledAppFlow.from_client_secrets_file(
#     'path_to_your_client_secret.json', SCOPES)

# creds = flow.run_local_server(port=8080)

# # Initialize the Chrome web driver
# service = ChromeService(executable_path='path_to_chromedriver')
# driver = webdriver.Chrome(service=service)

# # Set up the Gmail API service
# from googleapiclient.discovery import build

# service = build('gmail', 'v1', credentials=creds)

# # Example: Get the user's Gmail labels
# results = service.users().labels().list(userId='me').execute()
# labels = results.get('labels', [])

# if not labels:
#     print('No labels found.')
# else:
#     print('Labels:')
#     for label in labels:
#         print(label['name'])

# # Clean up
# driver.quit()

from google.oauth2.credentials import Credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from googleapiclient.discovery import build

# Step 1: Generate Access Token
credentials = Credentials.from_authorized_user_file('/home/arcgate/Desktop/selenium_project/client_secret_143443373358-gsa086lnq210g94jl1oj28o4le6f78ac.apps.googleusercontent.com.json')
credentials.refresh(None)
access_token = credentials.token

# Step 2: Automate Gmail Login with Selenium
driver = webdriver.Chrome()

driver.get('https://accounts.google.com/')

email_field = driver.find_element(By.NAME,'identifier')
email_field.send_keys('your_email@gmail.com')

next_button = driver.find_element(By.ID,'identifierNext')
next_button.click()

driver.implicitly_wait(10)
password_field = driver.find_element(By.NAME, 'password')

password_field.send_keys('your_password')

password_next_button = driver.find_element(By.ID,'passwordNext')
password_next_button.click()

# Step 3: Use Access Token for API Requests
service = build('gmail', 'v1', credentials=credentials)
labels = service.users().labels().list(userId='me').execute()

# Do something with the labels
for label in labels['labels']:
    print(label['name'])

# Close the WebDriver
driver.quit()
