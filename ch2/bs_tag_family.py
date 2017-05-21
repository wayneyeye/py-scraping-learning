from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import sys

url="http://www.pythonscraping.com/pages/page3.html"


def getChild(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html,"lxml")
        children = bsObj.find("table",{"id":"giftList"}).children
    except AttributeError as e:
        return None
    return children

for child in getChild(url):
    print(child)



def getDesc(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        desc = bsObj.find("table",{"id":"giftList"}).descendants
    except AttributeError as e:
        return None
    return desc

for desc in getDesc(url):
    print(desc)



def getNextSiblings(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        desc = bsObj.find("table",{"id":"giftList"}).tr.next_siblings
    except AttributeError as e:
        return None
    return desc

for sibl in getNextSiblings(url):
    print(sibl)
