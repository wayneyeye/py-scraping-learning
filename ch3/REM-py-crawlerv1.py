from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id ="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("") 


# sample output
# Wikipedia talk:Good article nominations
# <p>This is the <b>discussion</b> page of the <a href="/wiki/Wikipedia:Good_article_nominations" title="Wikipedia:Good article nominations">good article nominations</a> (GAN). To ask a question or start a discussion about the good article nomination process, click the New section link above. Questions may also be asked at the <a href="/wiki/Wikipedia:Good_article_help" title="Wikipedia:Good article help">GA Help desk</a>. To check and see if your question may already be answered, click to show the frequently asked questions below or search the archives below.</p>
# /w/index.php?title=Wikipedia_talk:Good_article_nominations&action=edit
