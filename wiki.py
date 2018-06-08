from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors 

resp= urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')
soup= BeautifulSoup(resp,"html.parser")
listurls= soup.find_all("a",href=re.compile("^/wiki/"))
for url in listurls:
    if not re.search("\.(jpg|JPG)$",url["href"]):
       print(url.get_text(),"<--->",url["href"])
