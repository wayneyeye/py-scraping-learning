from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import re, sys

url="http://en.wikipedia.org/wiki/Kevin_Bacon"

def getHrefTags(url,regexp):
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

for link in getHrefTags(url,"^(/wiki/)((?!:).)*$"): # ?! means does not contain 
    print(link.attrs["href"]) #print attribute src only!