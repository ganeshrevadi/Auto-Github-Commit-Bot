from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By

# GitHub API Key
api_key = 'Your API Key'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome('/path/to/chromedriver')

# Navigate to the GitHub login page
driver.get('https://github.com/login')

# Find the username and password fields
username_field = driver.find_element(By.ID,'login_field')
password_field = driver.find_element(By.ID,'password')

# Enter your GitHub credentials
username_field.send_keys('YOUR_USERNAME')
password_field.send_keys('YOUR_PASSWORD')

# Submit the login form
password_field.submit()

# Wait for the login process to complete (You may need to adjust the sleep time)
time.sleep(10)

# Navigate to the repository where you want to make a commit
driver.get('Url to the file you want to make a commit !')

time.sleep(10)  

edit_button = driver.find_element(By.LINK_TEXT,'Edit')
edit_button.click()


# Find the file content input field and clear its existing content
content_field = driver.find_element(By.ID,'editor')
content_field.send_keys(Keys.CONTROL + "a")
content_field.send_keys(Keys.DELETE)

# Enter the updated content for the file
content_field.send_keys('This is the updated content.')

# Find the "Commit changes" button and click it
commit_button = driver.find_element(By.XPATH,'//button[contains(text(), "Commit changes")]')
commit_button.click()

# Wait for the commit to be processed (You may need to adjust the sleep time)
time.sleep(5)
driver.quit()
print('Done!')