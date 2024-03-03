# WebScraper
from bs4 import BeautifulSoup
import requests
baseUrl = "https://www.bbc.com"
Url =  "https://www.bbc.com/news"
webPage = requests.get(Url)
#print(webPage.text)
soup = BeautifulSoup(webPage.content,"html.parser")
#print(soup.find('h2').text)
def normalScrape():
    h2tags=soup.find_all('h2')
    count =0
    for title in h2tags:
        count +=1

    print(count)
normalScrape()