from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

# Wrong URL
title = getTitle("http://www.pythonsscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
# Good URL
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)