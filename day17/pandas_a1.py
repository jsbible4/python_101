import pandas as pd

new_df = pd.read_csv('cgv_movieInformation.csv') # pd 로 데이터를 읽어달라는 뜻
# new_df.info()  # info 한 줄 요약 부탁
# new_df.describe()
print(new_df.describe())  # describe 한번 읊어봐라
#Name Memeber MovieName     Snacks  Time Transportation   Age
# count   1000    1000      1000       1000  1000           1000  1000
# unique   703       4        10         49     3              3     6            # 중복제거
# top      김도윤    플래티넘        윙카  팝콘이랑 물오징어    오후           대중교통   20대   # 가장 많이 중복된거
# freq       8     262       109         36   344            360   184            #

goldMembers = new_df[new_df['Memeber'] == '골드']
print(goldMembers)
time_counts = goldMembers['Time'].value_counts()  #빈도수 계산
print(time_counts)
print(goldMembers['Age'].value_counts())
most = time_counts.idxmax()  # 최빈값 계산
print(most)
movie_counts = goldMembers['MovieName'].value_counts()
print(movie_counts)
most_movie = movie_counts.idxmax()
print(most_movie)
