import pandas as pd

# 베송 목록 엑셀 파일 읽어오기
df = pd.read_excel('베송 목록.xlsx', sheet_name='베송 목록')

# 필요한 열만 추출하기
df = df[['운송장번호', '상품명', '받는 분 주소', '수량']]

# 열 이름 변경하기
df.columns = ['송장번호', '상품명', '주소', '수량']

# 주소 열을 구분자로 나누어 새로운 열 생성하기
new_cols = df['주소'].str.split(' ', n=3, expand=True)
df['수령인'] = new_cols[0]
df['주소1'] = new_cols[1]
df['주소2'] = new_cols[2]
df['주소3'] = new_cols[3]
df.drop('주소', axis=1, inplace=True)

# 택배사 엑셀 파일로 저장하기
df.to_excel('택배사 목록.xlsx', sheet_name='택배사 목록', index=False)
