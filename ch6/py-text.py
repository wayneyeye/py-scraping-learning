from urllib.request import urlopen
# textPage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# print(textPage.read())
# python character decoding

textPage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read(),"utf-8"))
