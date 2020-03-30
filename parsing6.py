from bs4 import BeautifulSoup

fp = open("fruits.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)

sel("#c")
sel("ul > li#a")