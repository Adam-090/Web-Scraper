# WebScraper
from bs4 import BeautifulSoup
import requests
Url =  "https://www.newegg.com"
webPage = requests.get(Url)
print(webPage.text)
soup = BeautifulSoup(webPage.content,"html.parser")
