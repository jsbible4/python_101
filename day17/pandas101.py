# import pandas
# from faker import Faker  #Faker 이름 뽑는 용.
#
# for i in range(100): #ja_JP : 일본어  #zh_CN : 중국어
#     a = Faker('ko_KR')
#     print(a.name())

# data = {
#     'Name' : ['이나은', '정동하', '최동준', '전수효'],
#     'Age' : [20,26,26,32],
#     'Coffee' : ['Latte','Vanilla','Hotchoco','Americano'],
# }
#
# a = pandas.DataFrame(data)
# a.to_csv('python_infomation.csv', index = False)
# 사람이름, 멤버쉽['브론즈','실버','골드','플래티넘'], 무엇을 봤다, 간식, 시간대, 이동수단[뚜벅이, 대중, 자차]
import pandas
import random
from faker import Faker
membership = ['브론즈','실버','골드','플래티넘']
movie = ['외계+인 2부','시민덕희','윙카','지오디 마스터피스','위시','덤머니','걸스 앤 판처','서울의 봄','인투더 월드','노량-죽음의 바다']
age = ['10대','20대','30대','40대','50대','60대']
snacks = ['팝콘이랑 물', '레몬에이드','감자튀김','오징어','팝콘','콜라','호두과자']
time = ['조조','심야','오후']
transpotation = ['뚜벅이','대중교통','자차']

name_list = []
membershipList = []
movieList = []
snacksList = []
timeList = []
transpotationList = []
ageList = []
for i in range(1000):
    name_list.append(Faker('ko_KR').name())
    membershipList.append(random.choice(membership))
    movieList.append(random.choice(movie))
    snacksList.append(random.choice(snacks)+random.choice(snacks))
    timeList.append(random.choice(time))
    transpotationList.append((random.choice(transpotation)))
    ageList.append((random.choice(age)))

movie = {
    'Name' : name_list,
    'Memeber' : membershipList,
    'MovieName' :movieList ,
    'Snacks' : snacksList,
    'Time' : timeList,
    'Transportation' : transpotationList,
    'Age' : ageList
}
a = pandas.DataFrame(movie)
a.to_csv('cgv_movieInformation.csv', index = False)
