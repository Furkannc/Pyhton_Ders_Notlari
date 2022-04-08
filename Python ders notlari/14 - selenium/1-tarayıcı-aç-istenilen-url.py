from selenium import webdriver
import time

browser=webdriver.Edge()
url="https://eksisozluk.com/sj--102493"
browser.get(url)
time.sleep(10)
browser.close()