import pandas
import pandas as pd  # dataFrame 이라는 class에 넣어서 지지고 볶고
# data type을 아는게 중요하다
import random  # command+option+l == 줄 맞춤 정렬. (전체 선택해서 ㅇㅇ)
from faker import Faker

faker = Faker('ko_KR')
# 이름 나잇대 성별 선택된 영화, 선택된 음료, 선택된 스낵 시간대
ages = [20, 30, 40, 50, 60]
agePercent = [30, 30, 20, 10, 10]
genders = ['male', 'female']
movies = ['웡카', '시민덕희', '너의 이름은', '도그맨', '외계인']
moviePrecent = [35, 20, 10, 5, 30]
snacks = ['일반팝콘', ' 카라멜팝콘', '어니언팝콘', '치즈팝콘', '나초', '오징어', '핫도그', '선택안함']
snacksPercent = [20, 10, 10, 10, 10, 5, 5, 30]
drinks = ['콜라', '제로콜라', '스프라이트', '제로스프라이트', '환타', '에이드', '아메리카노', '비타민음료', '물', '선택안함']
drinksPercent = [10, 20, 10, 20, 5, 5, 5, 5, 5, 5]
times = ['조조', '일반', '심야']
timesPercent = [20, 70, 10]
payments = ['현금', '체크 카드', '신용 카드', '카카오 페이', '계좌 이체', '토스 페이']
paymentsPercent = [5, 15, 50, 10, 10, 10]

data = {
    'name': [faker.name() for i in range(100)],  #
    'ages': [random.choices(ages, weights=agePercent, k=1)[0] for i in range(100)],
    # weights= 비율 의미  # k 뜻  # list 안에 숫자만 담아야 하니까 [0]
    'genders': [genders[random.randint(0, 1)] for i in range(100)],
    'movies': [random.choices(movies, weights=moviePrecent, k=1)[0] for i in range(100)],
    'payments': [random.choices(payments, weights=paymentsPercent, k=1)[0] for i in range(100)],
    'snacks': [random.choices(snacks, weights=snacksPercent, k=1)[0] for i in range(100)],
    'drinks': [random.choices(drinks, weights=drinksPercent, k=1)[0] for i in range(100)],
    'times': [random.choices(times, weights=timesPercent, k=1)[0] for i in range(100)]
}
df = pandas.DataFrame(data)
df.to_csv('cgv.csv', index=False)
