from selenium import webdriver

#For searching necessary in latest selinium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# executable_path='c:/Program Files (x86)/Google/chrome-win64/chrome.exe'

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

driver.maximize_window()

email = driver.find_element(By.XPATH , ".//input[@id='email']")
email.send_keys("rahulroxx460@gmail.com")
email.send_keys(Keys.RETURN)


time.sleep(3)

password = driver.find_element(By.XPATH , ".//input[@id='pass']")
password.send_keys('zebra@qwerty123')
password.send_keys(Keys.RETURN)




try:
    btn = driver.find_element(By.XPATH , ".//button[@id='login']")
    btn.click()
    time.sleep(6)

except:
    print("NOT FOUND")
finally:

    driver.get("https://www.facebook.com/profile.php?id=61579384046350")

    time.sleep(3)

    start = driver.find_element(By.XPATH , ".//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6']")
    start.click()

    time.sleep(5)
    p = driver.find_element(By.XPATH , ".//p[@class='xdj266r x14z9mp xat24cr x1lziwak x16tdsg8']")
    p.click()
    time.sleep(3)
    p.send_keys("Hey There This is a automation message i am trying to create Facebook Auto Poster trying and testing in selinium ")
    p.send_keys(Keys.RETURN)

    time.sleep(5)

    post = driver.find_element(By.XPATH , ".//div[@class='x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x14ldlfn x1b1wa69 xws8118 x5fzff1 x972fbf x10w94by x1qhh985 x14e42zd x9f619 xpdmqnj x1g0dm76 xwcfey6 x1r1pt67']")
    post.submit()

    time.sleep(40)

    driver.refresh()
    print("Work Done")