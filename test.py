# 한국어 형태소 분석
## 한국어 형태소는 결합되는 조사가 다양하고 많아서 분석이 힘들다
# 일반적으로 오픈소스인 형태소 분석 라이브러리를 가져다 사용하여 분석
# 이 라이브러리를 이용하면 형태소분석 알고리즘을 구현하지 않고 분석을 할 수 있다.
# 한국어 형태소 분석에 많이 사용되는 라이브러리 = KoNLPy 이다.

# KoNLPy 라이브러리 설치
# 1) JAVA 1.7 이상이 설치
# 2) Java Path 설정
# 3) JPype v0.5.7 이상의 패키지가 설치되어 있어야함. (자바를 파이썬에서 이용 할 수 있도록 하기위한 패키지)

#pip install --upgrade pip
#pip install jPype1
#pip install KoNLPy

#KoNLPy 라이브러리를 이용하면 꼬꼬마, Komoran, MeCab, Twitter 한나눔 등의 형태소 분석기를 사용 할 수 있다.

from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
pprint(kkma.nouns(u'명사만을 추출하여 워드클라우드를 그려봅시다'))