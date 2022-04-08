from selenium import webdriver
import time

browser=webdriver.Edge()
url="https://eksisozluk.com/sj--102493"
browser.get(url)
time.sleep(5)
contents=browser.find_elements_by_css_selector(".content")
for content in contents:
    print("***********************************")
    print(content.text)
browser.close()