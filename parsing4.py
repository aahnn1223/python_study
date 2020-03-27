## read로 불러올 때에는 바이너리 형태로 불러오기 때문에 우리가 읽기 어렵다.
import urllib.request

url="http://example.com/"

res = urllib.request.urlopen(url)

data = res.read()

#바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)