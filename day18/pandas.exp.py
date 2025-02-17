# pandas - python으로 스프레드시트를 다루는 도구
# series[하나의 열],dataframe[n개의 열]  판다스에서 제공하는 data타입   # series가 모여 dataframe이 된다.
import pandas as pd


# 판다스에서 데이터 불러오기
df = pd.read_csv('lex.csv')
print(df.shape)  # shape (195, 302) (행, 열)
print(df.columns) # 열
# 판다스에서 데이터 타입 object == string 이다.

# 판다스에서 데이터 추출하기
print(df.head()) # 위에 5개 행 뽑기
print(df.tail()) # 뒤에서 5개 행 뽑기

print(df[['2024','2025','2026']]) # 여러 열 뽑기
print(df['2024']) # 하나 열 뽑기   # series 타입
#print(df['Turkey'])  #행은 이거로 출력이 안됨.

print(df['country']) # country 도 열이었음

