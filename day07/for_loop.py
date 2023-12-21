#num = int(input("몇번 반복 할까요: "))


#for index in range(num):    #() 안에 들어갈 숫자는 몇 번 반복할 지를 정한다.
 #i는 몇 번째인지 알려주는 역할 . ==index
    #print(f"{index}, 메가스터디는 현우진이 짱이다.")

#num = int(input("몇번 반복 할까요: "))

#for index in range(num):    #num 은 0번부터 시작이다.
 #   if index % 105==0:           #조건 설정 가능
  #      print(index)

#loop = int(input("몇번 반복 할까요:"))
#first = int(input("첫번째 자연수를 입력하세요:"))
#second = int(input("두번째 자연수를 입력하세요:"))
#for index in range(loop):
#    if index % first ==0 and index %second == 0:  #공배수
 #       print(index)

# 구구단 출력 하기
# 몇 단을 출력할까요? : 3
# 3 * 1 = 3 ... 3 * 9 = 27

#dan = int(input("몇 단을 출력할까요?"))
#for index in range(1,10):
#    print(f"{dan} * {index} = {index*dan}")


num = [1, 2, 3, 4, 5]
for i in num:
    print(i)

#text = "python"
#for i in text:
#    print(i)

# 1. range() 사용해서, 빈리스트에 0~100 사이의 정수를
# 5개 넣어주는 코드를 작성하세요.
# [] -> [1, 3, 4, 5, 6]

import random
list = []
for i in range(5):
    a = random.randint(0,100)
    list.append(a)
print(list)

#for i in list:
#    print(i)
#가장 큰 숫자 고르기

#1번째 방법
#list.sort()       #리스트에서 오름차순으로 정렬
#print(f"{list[-1]}")  # 맨 뒤의 숫자를 고른다.

#2번째 방법
#
max = list[0]
for i in list:
    if max<i:
        max = i    # max를 계속 갱신해주는 작업.
print(max)

least = list[-1]
for i in list:
    if least>i:
        least=i
print(least)

fruit_dict = {
    1 : 'stawberry',
    2:'lemon',
    3: 'apple',
    4: 'pineapple',
    5: 'banana'
}
fruits = []
for i in range(10):
    rand = random.randint(1,5)
    fruits.append(fruit_dict[rand])

print(fruits)   #이모지 = 시작버튼(윈도우즈 버튼) 누르고 .

for i, v in enumerate(fruits):   #
    print(i, v)