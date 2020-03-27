from konlpy.tag import Twitter

twitter = Twitter() # 트위터 객체 설정

# Twitter 객체의 pos() 메소드를 이용
# pos(분석할 문장, norm옵션, stem옵션)
# norm : 오타가 있을 때 정확하게 표기를 해주는 옵션
# stem : 원형을 찾아주는 옵션


## wordList = twitter.pos("친구가 집에 놀러 왔다",norm=True,stem=True)
##print(wordList)


# 한나눔 분석기(Hannanum)
from konlpy.tag import Hannanum
hannanum = Hannanum()

## wordList = hannanum.analyze(u'롯데마트의 흙마늘 양념 치킨이 논란이 되고 있다.')
##print(wordList)

wordList = hannanum.morphs(u'롯데마트의 흙마늘 양념 치킨이 논란이 되고 있다.')
nounList = hannanum.nouns(u'다람쥐 새 쳇바퀴에 타고싶어')
print(wordList)
print(nounList)
print(hannanum.pos(u'웃으면 더 행복합니다'))