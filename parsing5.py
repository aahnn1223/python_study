from bs4 import BeautifulSoup
import urllib.request as req

url = "https://github.com/shin285/KOMORAN"

res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser")

##title = soup.find("title").string
##print(title)


