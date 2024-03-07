# WebScraper
from bs4 import BeautifulSoup
import requests
import sys 
mode=""
type=""


typearg = sys.argv[2:]
# This is the part of the code that takes in command line arguments.
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
# Webscraping Code
webPage = requests.get(Url)
#bs4 object
soup = BeautifulSoup(webPage.content,"html.parser")
#fucnction for scraping
def normalScrape():
    #finds all the h2 tags
    h2tags=soup.find_all('h2')

  #loops through the list and prints out the new titles
    for title in h2tags:

        print(title.text)

normalScrape()
    


