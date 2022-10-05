import selenium as sel
import requests as req
from bs4 import BeautifulSoup

url = "https://shop.nag.ru/search?search=Cisco%20Catalyst%20C9200L-24P-4G-E"
resp = req.get(url)
soup = BeautifulSoup(resp.text, "lxml")
tag = soup.findAll(class_="jsx-4270954716")
print(tag)

