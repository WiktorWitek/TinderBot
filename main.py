from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.get("https://tinder.com/")

time.sleep(2)
log_in_button = driver.find_element(By.XPATH, "//*[@id='s-1432688076']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
log_in_button.click()

time.sleep(2)
fb_login = driver.find_element(By.XPATH, "//*[@id='s-1211347640']/main/div/div/div[1]/div/div/div[3]/span/div[2]/button")
fb_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(2)
cookies = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]")
cookies.click()

time.sleep(1)
email_ = driver.find_element(By.ID, "email")
pass_ = driver.find_element(By.ID, "pass")
email_.send_keys("") # Your login
pass_.send_keys("") # Your password
time.sleep(1)
pass_.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)


time.sleep(10)
location = driver.find_element(By.XPATH, "//*[@id='s-1211347640']/main/div/div/div/div[3]/button[1]")
location.click()

time.sleep(3)
noti = driver.find_element(By.XPATH, "//*[@id='s-1211347640']/main/div/div/div/div[3]/button[2]")
noti.click()

time.sleep(3)
cookies2 = driver.find_element(By.XPATH, "//*[@id='s-1432688076']/div/div[2]/div/div/div[1]/div[1]/button")
cookies2.click()

time.sleep(2)

# Type start before script start swiping right so you can change location before
s = input("Type 'start': ")

body = driver.find_element(By.TAG_NAME, 'body')
if s == "start":
    for _ in range(10):
        time.sleep(2)
        body.send_keys(Keys.ARROW_RIGHT)