from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import re, sys, random, datetime

url="http://en.wikipedia.org/wiki/Kevin_Bacon"
regexp="^(/wiki/)((?!:).)*$"

def getLinks(url,regexp):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html,"lxml")
        hrefs = bsObj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile(regexp)}) # use find all here
    except AttributeError as e:
        return None
    return hrefs

# for link in getLinks(url,regexp): # ?! means does not contain 
#     print(link.attrs["href"]) #print attribute src only!

wikiheading="https://en.wikipedia.org"

links=getLinks(url,regexp)
while len(links) > 0:
	newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
	print(newArticle)
	links=getLinks(wikiheading+newArticle,regexp)
