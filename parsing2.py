"""" 
    urlopen 함수는 urllib.request패키지 안에 포함 되어 있음
    : HTTP를 통해 웹서버에 데이터를 얻어올 때 많이 사용하는 함수

    urlopen(url, [,data[,timeout]])  : [] 는 생략 가능
    - url : 열고자 하는 url 문자열
    - data: POST 방식으로 전송 시에 서버로 업로드할 폼 데이터
    - timeout: 타임아웃 시간


    urlopen() 지원되는 메소드
     urlopen().read([nbyte]) : nbyte의 데이터를 바이트 문자열로 읽음
     urlopen().readline() : 한 줄의 텍스ㅡ를 바이트 문자열로 읽음
     urlopen().info() : url에 연관된 메타 정보를 담은 매핑 객체를 반환
     urlopen().getcode() : HTTP 응답 코드를 정수로 반환 (있으면 200, 없으면 404)
     urlopen().close(): 연결을 닫는다.
"""

import urllib.request

url = "https://github.com/aahnn1223/python_study"
u = urllib.request.urlopen(url)
# read() 바이트 문자로 변환해서 가져오는 함수
## print(u.read())

print(u.info())