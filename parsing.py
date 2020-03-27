"""
[ beautifulsoup 사용 ]
HTML, XML 파일에서 데이터를 읽어내는 파이썬 라이브러리

"""

html_doc = """
<html><head><title>옛날 이야기</title></head>
<body>
<p class = "title"><b>옛날 이야기</b></p>

<p class = "story">옛날 옛적에 세명의 자매가 있었습니다.
    <a href = "http://example.com/elsie" class = "sister" id = "link1">엘리제</a>
    <a href = "http://example.com/lacie" class = "sister" id = "link2">레이시</a>
    <a href = "http://example.com/tillie" class = "sister" id = "link3">타일리에</a> 이었습니다.
    그들은 아주 가난하게 살았습니다.

</p>
<p class = "story">...............</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoup 생성자
# 생성자에서는 html_doc를 파싱하고 그 결과를 BeautifulSoup 객체에 반환

## print(soup.prettify()) #prettify 함수는 Beautifulsoup에서 파싱 처리한 파서트리를 유니코드로 리턴하는 함수
## print(soup.title)
## print(soup.title.name)
## print(soup.title.string)
## print(soup.title.parent.name)
## print(soup.p)
## print(soup.p['class'])

## print(soup.find_all('a'))
## print(soup.find(id="link2"))

for link in soup.find_all('a'):
    print(link.attrs['href'])
#    print(link.get('href'))

a = soup.a
print(type(a.attrs))



## txt = soup.get_text()
## print(txt)

## print(soup.head.title.string)
# 형제관계 = sibling 이라고 한다.

p1 = soup.p
## print(p1)
p2 = p1.next_sibling.next_sibling
## print(p2)
p3 = p2.previous_sibling
## print(p3)
p4 = p3.previous_sibling
## print(p4)