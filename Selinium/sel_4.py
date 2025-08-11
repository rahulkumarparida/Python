from selenium import webdriver

#For searching necessary in latest selinium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# executable_path='c:/Program Files (x86)/Google/chrome-win64/chrome.exe'

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

time.sleep(5)


try:
    btn = driver.find_element(By.CLASS_NAME , "a-button-text")
    btn.click()
except :
    print('OK')
    
finally:

    # input = driver.find_element(By.ID , "twotabsearchtextbox")
    input = driver.find_element(By.XPATH , "//input[@id='twotabsearchtextbox']")

    input.send_keys('Anime Merchedaise')
    input.send_keys(Keys.RETURN)

    time.sleep(5)

    btn = driver.find_element(By.ID , "nav-search-submit-button")
    btn.click

    list = driver.find_elements(By.XPATH , "//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal']")


    time.sleep(10)


    print(list , ' Products Found')

    for i in list:
        print(i.text ,' \n')

    driver.quit()