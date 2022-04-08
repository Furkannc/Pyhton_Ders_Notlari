from asyncore import write
from selenium import webdriver
import time
from keyboard import press

file=open("twitts.txt","a",encoding="utf-8")
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
time.sleep(3)
go=browser.get("https://twitter.com/explore")
time.sleep(2)
search=browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').send_keys("#dolar")
time.sleep(1)
press("enter")
time.sleep(5)
contents=browser.find_elements_by_css_selector(".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")

twits=[]
for content in contents:
    if(len(content.text)>30):
        twits.append(content.text)
browser.close()
numb=1
for i in twits:
    content=str(numb) + " - " + i + "\n"
    file.write(content)
    numb+=1
