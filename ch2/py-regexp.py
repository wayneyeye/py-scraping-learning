from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import re, sys

url="http://www.pythonscraping.com/pages/page3.html"

def getImg(url,regexp):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html,"lxml")
        images = bsObj.findAll("img",{"src":re.compile(regexp)}) # use find all here
    except AttributeError as e:
        return None
    return images

for image in getImg(url,"\.\.\/img\/gifts\/img.*\.jpg"):
    print(image)