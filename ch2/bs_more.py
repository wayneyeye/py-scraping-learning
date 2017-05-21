from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import sys

# html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj=BeautifulSoup(html,'lxml')
# print(bsObj.h1)


def getGreens(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        nameList = bsObj.findAll("span",{"class":"green"})
    except AttributeError as e:
        return None
    return nameList

for name in getGreens("http://www.pythonscraping.com/pages/warandpeace.html"):
	# this is to get html tags
	# print(name)
	# this is to get rid of the tags and leave the texts only
	print(name.get_text())
