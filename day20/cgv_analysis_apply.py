import pandas as pd

df = pd.read_csv('cgv.csv')

print(df.columns)

#50 or 60 가 팝콘을 고른다면, 팝콘 할인 -> 해당 / 안됨

def recommendPopcornForSenior(row):
    if row['ages'] == 50 or row['ages'] == 60:
        return '할인 대상'
    else:
        return '없음'

df['어르신 스낵 할인'] = df.apply(recommendPopcornForSenior,axis=1)  # recommendPopcornForSenior 에 ()를 넣으면 이미 실행된 함수임. # callback 함수
print(df)
