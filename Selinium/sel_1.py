from selenium import webdriver

#For searching necessary in latest selinium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# executable_path='c:/Program Files (x86)/Google/chrome-win64/chrome.exe'

driver = webdriver.Chrome()

driver.get("https://www.google.com")

input = driver.find_element(By.NAME,'q')
input.send_keys('Food')
input.send_keys(Keys.RETURN)

print(driver.title)

button = driver.find_element(By.CLASS_NAME , 'plR5qb')
button.click()

time.sleep(5)

driver.back()
time.sleep(5)
driver.forward()

time.sleep()
driver.quit()


