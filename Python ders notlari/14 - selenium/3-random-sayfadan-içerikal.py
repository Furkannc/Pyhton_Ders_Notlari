from selenium import webdriver
import time
import random


entries=[]
browser=webdriver.Edge()
url="https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pageCount=1
while(pageCount<=10):
    number=random.randint(1,2267)
    newUrl=url+str(number)
    browser.get(newUrl)
    time.sleep(2)
    contents=browser.find_elements_by_css_selector(".content")
    for i in contents:
        entries.append(i.text)
    pageCount+=1 

count=1
browser.close()
for i in entries:
    print(str(count)+"//////////////////////////////////")
    print(i)
        

    count+=1

