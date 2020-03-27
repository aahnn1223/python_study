# KoNLPy 패키지에 있는 분석기(형태소, POS 태그 작성기)
''' 
카이스트에서 by 자바, jdk가 설치 되어 있어야 함.
 Hannanum Class
  - analyze(구문) : 구문 분석
  - morph(구문) : 형태소 분석
  - nouns(구문) : 명사 추출
  - pos(구문, 옵션) 
'''

'''
 Kkma Class
  - morphs()
  - nouns()
  - pos()   
'''

'''
by 자바, jdk가 설치되어 있어야 함.
 Komoran Class
  - morphs()
  - nouns()
  - pos()
'''

'''
 Okt class : 기존의 Twitter Class가 Okt Class로 변경됨.
 by 스칼라
   - morphs()
   - nouns()
   - pos()
   - phrases() : phrase 추출
'''
#Komoran 사용
# 사용자 사전을 만들 수 있다는 특징이 있다

'''
    품사 (POS : Part Of Speech)

    NN(명사) : NNP(고유명사), NNG(일반명사)
    VV(동사), VCN(부정지정사, 형용사)
'''

## from konlpy.tag import Komoran

## komoran = Komoran(userdic='dic.txt') # userdic : 사용자 정의 사전 경로명

## wordList = komoran.morphs(u'와우 코모란도 오픈소스가 되었습니다')
## wordList = komoran.nouns(u'오픈소스에 관심이 많은 멋진 개발자들')
## wordList = komoran.pos(u'혹시 바람과 함께 사라지다 보셨나요?')
## print(wordList)


# Okt Class 사용

from konlpy.tag import Okt
okt = Okt()

## wordList = okt.morphs(u'단독 입찰보다 복수 입찰의 경우')
## wordList = okt.nouns(u'유일하게 항공이 체계 종합개발 경험을 갖고 있는 KAI는')
## wordList = okt.phrases(u'날카로운 분석과 신뢰감 있는 진행으로')

## wordList = okt.pos(u'이것도 되놔욬ㅋ')
## wordList = okt.pos(u'이것도 되놔욬ㅋ',norm=True)

wordList = okt.pos(u'이것도 되놔욬ㅋ', norm=True, stem=True)
print(wordList)










