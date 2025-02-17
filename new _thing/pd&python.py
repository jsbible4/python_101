import pandas as pd
data = {
    '판다스 자료형' : ['object', 'int64','float64','datetime64'],
    '파이썬 자료형' : ['string', 'int', 'float', 'datetime'],
    '설명' : ['문자열', '정수', '소수점을 가진 숫자', '파이썬 표준 라이브러리인 datetime이 반환하는 자료형']
}
df = pd.DataFrame(data)
df.to_csv('pandasAndpython.csv', index=False)
