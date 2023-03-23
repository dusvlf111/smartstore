import requests
from bs4 import BeautifulSoup

# 로그인 정보
LOGIN_INFO = {
    'id': '네이버 아이디',
    'pw': '네이버 비밀번호'
}

# 세션 생성
with requests.Session() as s:
    # 로그인 페이지 가져오기
    login_page = s.get('https://nid.naver.com/nidlogin.login')
    # 로그인 페이지의 HTML 파싱
    soup = BeautifulSoup(login_page.text, 'html.parser')
    # 로그인에 필요한 정보 가져오기
    LOGIN_INFO['encpw'] = soup.select_one('#enc_login_password')['value']
    LOGIN_INFO['encnm'] = soup.select_one('#encnm')['value']
    LOGIN_INFO['locale'] = 'ko_KR'
    # 네이버 로그인하기
    login_result = s.post('https://nid.naver.com/nidlogin.login', data=LOGIN_INFO)
    
    # 스마트스토어 페이지 가져오기
    store_page = s.get('https://sell.smartstore.naver.com/#/home')
    # 스마트스토어 페이지의 HTML 파싱
    soup = BeautifulSoup(store_page.text, 'html.parser')
    # 엑셀 파일 다운로드 링크 가져오기
    excel_link = soup.select_one('a[href*="/Product/ExcelDownload"]')['href']
    # 엑셀 파일 다운로드 링크에 세션 정보 추가
    excel_link = s.get('https://sell.smartstore.naver.com' + excel_link).url
    
    # 엑셀 파일 다운로드
    excel_file = s.get(excel_link)
    # 엑셀 파일 저장
    with open('smartstore.xlsx', 'wb') as f:
        f.write(excel_file.content)
