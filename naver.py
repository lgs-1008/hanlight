import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.naver.com/"
html = requests.get(url).text #네이버의 소스코드를 받아옵니다.
soup = BeautifulSoup(html, 'html.parser') #크롤링을 위해 BeautifulSoup를 사용했습니다.
s = soup.select('.PM_CL_realtimeKeyword_rolling span[class=ah_k]') #실시간 검색어 부분만 골라서 저장합니다.
time = datetime.datetime.now() #현 시각 출력을 위해 시간을 저장합니다.

print( #시간 출력. 한글포멧을 위해 인코딩과 디코딩 과정을 거쳐줍니다.
    time.strftime('\n%Y년 %m월 %d일 %H시 %M분\n네이버 실시간 검색어\n'.encode('unicode-escape').decode()).encode().decode('unicode-escape')
)

print(s)

for i,s in enumerate(s): #실시간 검색어s를 나열하여 출력해줍니다.
    print(s.text)
