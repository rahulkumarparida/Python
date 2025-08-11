from selenium import webdriver

#For searching necessary in latest selinium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# executable_path='c:/Program Files (x86)/Google/chrome-win64/chrome.exe'

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

time.sleep(5)

driver.refresh()

time.sleep(5)