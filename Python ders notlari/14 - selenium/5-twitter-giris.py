from selenium import webdriver
import time
from keyboard import press


browser=webdriver.Edge()
browser.get("https://twitter.com/")
time.sleep(2)
sign=browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span").click()
time.sleep(3)
name=browser.find_element_by_name("text").send_keys("furkangobrr")
time.sleep(1)
press("enter")
press("enter")
time.sleep(2)
passw=browser.find_element_by_name("password").send_keys("5747Fc..")
time.sleep(1)
press("enter")
press("enter")
time.sleep(30)

browser.close()

