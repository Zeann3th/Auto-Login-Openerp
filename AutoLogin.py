# Importing Libs
import os
import time
from selenium import webdriver

os.environ['PATH'] += r"D:\Workspace\PycharmProjects\PyWorkspace\SeleniumDrivers\geckodriver-v0.33.0-win32\geckodriver.exe"
driver = webdriver.Firefox()
# Entering the page
driver.get("https://openerp.dailyopt.ai/login")
driver.implicitly_wait(10)

# Fill-in Username & Password
username = driver.find_element("id", "user")
username.send_keys(" ")  # Your Username here

password = driver.find_element("id", "password")
password.send_keys(" ")  # Your Password here

# Hitting the login button
login = driver.find_element("xpath", "//*[text()='Login']")
login.click()
time.sleep(10)
# Quit browser
driver.quit()
