# urlopen() 을 이용해서 파일 저장

import urllib.request
import ssl

context = ssl._create_unverified_context()

url = "https://t1.daumcdn.net/cfile/tistory/213B5437527F8C6311"

# 메모리에 다운로드 함
mem = urllib.request.urlopen(url).read()
 ## read로 불러올 때에는 바이너리 형태로 불러오기 때문에 우리가 읽기 어렵다.

save_img = "python.png"

# 파일로 저장
with open(save_img, mode="wb") as f:  #wb : write binary
    f.write(mem)
    print("해당 파일이 저장 되었습니다.")