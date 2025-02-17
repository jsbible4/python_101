import pandas as pd

df = pd.read_csv('cgv.csv')
print(df)


# group by
# print(df.columns)
# # ages
# group_by_ages = df.groupby('ages')
# movies_by_ages = group_by_ages['movies'].value_counts() # 나잇대 별로 선호하는 영화
# print(movies_by_ages)
#
#
# payments_by_ages = group_by_ages['payments'].value_counts() # 나잇대 별로 선호하는 결제방식
# print(payments_by_ages)
#
#
# #times
# group_by_times = df.groupby('times')
# drinks_by_times = group_by_times['drinks'].value_counts()
# print(drinks_by_times)
#
# most_drinks_by_times = group_by_times['drinks'].value_counts().groupby(level=0).head(1)  # level=0times, # head(n) n번째 까지 뽑기
# print(most_drinks_by_times)
#
# #snacks
# snacks_by_ages = group_by_ages['snacks'].value_counts() # 나잇대 별로 선호하는 결제방식
# print(snacks_by_ages)

import matplotlib.pyplot as plt

## 시간대별 음료 데이터 시각화 # donut
# group_by_times = df.groupby('times')
# drinks_by_times = group_by_times['drinks'].value_counts()
# print(drinks_by_times['조조'])
# morning_times_snacks = drinks_by_times['조조']
# # 조조 시간대의 음료
# import matplotlib.pyplot as plt
# from matplotlib import rc
# import seaborn as sns
# # %matplotlib inline
# rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False
# plt.pie(morning_times_snacks, labels=morning_times_snacks.index, autopct='%1.1f%%') #autopct = 비율 알려줌
# plt.show()
# print(morning_times_snacks.index)

# 간식 갯수

grouped_data = df[df['snacks'] == '일반팝콘']['drinks'].value_counts()
chart_data = pd.DataFrame(grouped_data).reset_index()
chart_data.columns = ['Drinks', 'Count']

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(10, 6))
plt.bar(x='Drinks', y= 'Count', )
plt.title('음료별 일반팝콘 구매 빈도')
plt.xlabel('음료')
plt.ylabel('빈도')
plt.show()


# plt.bar(normalPopcorn_drinks)
# plt.xlabel('drinks')
# plt.ylabel('counts')
# plt.show()

#이변
# plt.bar(keys,value)
# plt.xlabel('station')
# plt.ylabel('bicycle')
# plt.show()




