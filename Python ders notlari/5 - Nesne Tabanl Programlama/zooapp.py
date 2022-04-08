import requests

from bs4 import BeautifulSoup

url="https://eksisozluk.com/hayatta-ogrenilenler--205618"

response=requests.get(url)

icerik=response.content

soup=BeautifulSoup(icerik,"html.parser")

for i in soup.find_all("a"):
    print(i)
