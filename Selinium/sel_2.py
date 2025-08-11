from selenium import webdriver

#For searching necessary in latest selinium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# executable_path='c:/Program Files (x86)/Google/chrome-win64/chrome.exe'

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

try:
    btn = driver.find_element(By.CLASS_NAME , "a-button-text")
    btn.click()
except :
    print('OK')
    
finally:
    time.sleep(5)

    select = driver.find_element(By.LINK_TEXT, "Electronics")
    select.click()

    next = driver.find_element(By.LINK_TEXT , "Audio")
    next.click()

    time.sleep(10)