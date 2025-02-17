import pandas
import matplotlib.pyplot as plt
# python을 이용한 데이터 시각화 라이브러리 = matplotlib
megacoffee = {
    'name': [ '아메리카노', ' 라떼', '바닐라', '맥심', '디카페인'],
    'price': [ 2500, 3000, 3500, 3000, 4000],
    'caffeine': [150,100,120,100,0]
}

# 히스토그램 일변량
# data = [5,4,3,2,1,2,3,4,5,3,4]
# plt.hist(data,color='skyblue')
# plt.show()


# 막대그래프 이변량
# plt.subplot(2,3,2)
# plt.bar(['A', 'B', 'C', 'D'], [10,20,30,40])
# plt.show()


# df = pandas.DataFrame(megacoffee)  # dictionary 형태를 dataframe 타입으로 바꿨다는 뜻
# plt.plot(megacoffee['caffeine'], megacoffee['price'])
# plt.show()


# x = [1,2,3,4,5]
# y = [30,20,10,20,10]
#
# plt.plot(x,y)
#
# plt.show()  # 함수 나옴.

# print(f'column: {df.columns}')  # 열 보여줌
# print(f'index {df.index}')
# print(f'value: {df.values}') # 행 보여줌
#
# # 추출하기
# name_column = df['name']
# print(f'names: {name_column}')
# print(type(name_column))
# import pandas

df1 = pandas.read_csv('Seoul_bicycle.csv', encoding='cp949') # 한글을 나타내는 방식 = cp949 (다른 방식들도 있다)
print(df1.columns)
print(df1.index)
print(df1.values)

data = df1['시작_대여소명'].tolist() # 원래 series 차입이었는데 list화 시켜준다.
# places = {}
# for i in data:
#     only_dong = i.split('_')[0]
#     if only_dong in places:
#         places[only_dong] += 1
#     else:
#         places[only_dong] = 1
# print(places)
# sortedPlaces = dict(sorted(places.items()))
# # sorted라는 내장함수: 매개변수로 들어온 이터러블한 데이터를 새로운 정렬된 리스트로 만들어서 반환해 주는 함수
# # 리스트.sort()와 sorted(리스트)의 가장 큰 차이는리스트.sort()는 본체의 리스트를 정렬해서 변환하는 것이고,
# # sorted(리스트)는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다.
# # 따라서 출력된 list를 dict화 시켜줘야 하는 것이다.
# print(sortedPlaces)

import random
# randomName = []
# for i in data:
#     only_dong = i.split('_')[0]
#     if not random.choice(only_dong) in randomName:
#         randomName.append(random.choice(only_dong))
# print(randomName)
# print(only_dong)


keys = list(sortedPlaces.keys())
value = list(sortedPlaces.values())


# 원그래프 일변량
plt.pie(value)
plt.show()

#이변
# plt.bar(keys,value)
# plt.xlabel('station')
# plt.ylabel('bicycle')
# plt.show()


