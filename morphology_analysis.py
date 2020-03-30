# textfile.txt = 혈의 누

# codesc 는 문서를 불러오기 위한 패키지
# 이전에는
# with open("aaa.txt", "rb") as input:
# data = input.read()
# 이후에 인코딩을 해줬었음.
# 데이터가 작은 경우엔 사용 할 수 있었음.
# 용량이 큰 파일을 다룰 때는 모든 데이터가 메모리에 로드되기 때문에 파일처리시 문제가 발생
# 이런 문제점을 해결하기 위해서는 파일을 조금씩 읽고, 메모리에도 약간의 데이터만 로드를 할 수 있다. (codecs 모듈 이용)

# Stream 방식
# 입력 Stream
# input = codecs.open("aaa.txt", "rb", encoding="utf-16")

import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

fp = codecs.open("textfile.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
okt = Okt()
body = soup.select("body > p")
# body = soup.select_one("body > p")
# text = body.getText()

word_dic = {}
for p in body:
    text = p.string
    wordList = okt.pos(text)
    for word in wordList:
        # 명사만을 추출해서 출현 횟수 카운팅 작업
        if word[1] == "Noun":
            if not(word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] = word_dic[word[0]] + 1
# 빈도수가 많은 순으로 50개의 명사를 출력
keys = sorted(word_dic.items(), key= lambda x:x[1], reverse = True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")

