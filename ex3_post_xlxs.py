import requests
import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel('배송엑셀파일이름.xlsx')

# 택배사에게 보낼 데이터 만들기
data = df.to_dict('records')

# 택배사에게 HTTP POST 요청 보내기
url = 'http://택배사홈페이지주소'
response = requests.post(url, json=data)

# 송장번호 받아오기
response_data = response.json()
tracking_numbers = [item['송장번호'] for item in response_data]

# 송장번호 엑셀 파일에 추가하여 저장하기
df['송장번호'] = tracking_numbers
df.to_excel('배송엑셀파일이름.xlsx', index=False)
