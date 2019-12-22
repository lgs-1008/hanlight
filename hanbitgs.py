from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import getpass

options = webdriver.ChromeOptions() #브라우저가 열리지 않게 헤드리스로 작동하게끔 해주는 코드.
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

print('아이디를 입력해주세요.')
ID = input()
print('비밀번호를 입력해주세요.')
PW = getpass.getpass()

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
driver.implicitly_wait(2) # 2초만 기다리겠습니다.

driver.get('https://www.hanlight.kr/user/login') #로그인링크

driver.implicitly_wait(2)

id = driver.find_element_by_name('id') #아이디와 비밀번호 요소를 찾는 코드
pw = driver.find_element_by_name('password')

id.clear() #아이디 입력부분
id.send_keys(ID)

pw.clear() #비밀번호 입력부분
pw.send_keys(PW)

driver.find_element_by_xpath("//*[@id='root']/div/div/form/button").send_keys(Keys.ENTER) # 입력한 아이디, 비밀번호 전송

time.sleep(2) #로그인 기다리기

try:
    driver.get('https://www.hanlight.kr/meal') #월별 급식을 크롤링 하기 위해 급식탭으로 이동

    z = [2,3,4,5,6] #코드를 분석해보니 첫주는 2부터 시작했음.
    x = [1,2,3,4,5] #월화수목금

    for i in z: #주 변경
        for y in x: #요일 변경
            xpath_gs = '//*[@id="root"]/div/div[3]/div/div[' + str(z[i-2]) +']/div[2]/div/div[' + str(x[y-1]) + ']'
            gs = driver.find_element_by_xpath(xpath_gs).text #주와 요일에 맞게 xpath수정후 조회하고 텍스트로 가져옴
            print(gs) #출력
            print("\n")

        print("\n") #주 별로 들여쓰기 추가

except:
    print("아이디나 비밀번호가 틀렸거나 인터넷 연결상태가 불안정합니다.")

driver.quit() #드라이버 종료
