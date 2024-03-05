# WebScraper
from bs4 import BeautifulSoup
import requests
import sys 
mode=""
type=""


typearg = sys.argv[2:]

for arg in typearg:
    if arg == "-m":
        mode = "normal"
    elif arg == "-n":
        type = "news"
    elif arg == "-t":
        type = "travel"
    elif arg == "-b":
        type = "business"
    elif arg == "-c":
        type = "culture"
    elif arg == "-e":
        type = "earth"
    
    
        



if type == "":
    type = "news"
if mode == "":
    mode = "normal"



baseUrl = "https://www.bbc.com"
Url =  ""

if type == "news":
    Url = baseUrl +"/news"
elif type == "travel":
    Url = baseUrl + "/travel"
elif type == "business":
    Url = baseUrl + "/business"
elif type == "culture":
    Url = baseUrl + "/culture"
elif type == "earth":
    Url = baseUrl + "/future-planet"

webPage = requests.get(Url)
#print(webPage.text)
soup = BeautifulSoup(webPage.content,"html.parser")
#print(soup.find('h2').text)
def normalScrape():
    h2tags=soup.find_all('h2')
  
    for title in h2tags:

        print(title.text)

normalScrape()
    


