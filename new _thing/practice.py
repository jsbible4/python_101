soccer = ['Heechan', 'Heungmin', 'Gangin' ]
print(type(soccer))
print(soccer[2])

article = """Main opposition party leader Lee Jae-myung was attacked by an assailant and stabbed in the neck by a knife during his tour to Busan on Tuesday morning.
Lee was stabbed around 10:27 a.m. after talking to reporters during a visit to the site of a new airport off the coast of Busan. The assailant was detained by police at the scene.
Lee sustained a cut 1 centimeter-wide and remained conscious when the paramedics arrived at the scene, emergency authorities said, adding that his injuries did not appear to be life threatening.
The main opposition leader was rushed to Pusan National University Hospital located in southern Busan by helicopter some 20 minutes after the stabbing. After receiving emergency treatment in Busan, he was airlifted to Seoul National University Hospital around 1 p.m. for surgery."""

article_list = article.split()
article_list.sort()
print(article_list)
print(article_list[30:])
import random

print(random.choice(article_list))
print(random.shuffle(article_list))

set = {1,2,3,4,5,6,7,8,7,6,5,4,3,32}
set2 = {567,45,34,77,22,2,33,44566}
print(set.symmetric_difference(set2))


capital = {
"korea" : "seoul",
"china" : "beijing",
"malaysia" : "kuala lumpur",
"USA" : "washington DC"
}
print("korea" in capital)

for i in range(1,24,2):
    print(i)
for i, f in enumerate([1,2,3,4,5,6,7,8,9]):
    print(i,f)


# 1. range() 사용해서, 빈리스트에 0~100 사이의 정수를
# 5개 넣어주는 코드를 작성하세요.
# [] -> [1, 3, 4, 5, 6]
import random
list = []
for i in range(5):
    random_number = random.randint(0,100)
    list.append(random_number)

print(list)
list.sort()
print(list[-1])

max = list[0]
for i in list:
    if max < i:
        max = i
print(max)

a = [i**2 if i%2==0 else i*3 for i in list]
print(a)
#반복문 for 챌린지!
#제일 많은 과일은 ~~, 제일 적으 ㄴ과일은 ~~~ 출력하는 코드.
import random

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

print(i)

# a = random.randint(1,5)
# numer = fruit_dict[a]
#
# for i in fruit_dict:
#     if fruits.count(i) < fruits.count(numer):
#

# print("이 리스트에서 가장 많이 나온 과일은")

# 해결은 나중에 뭐 배우면..


for i in range(100):
    if i % 2 == 0:
        break
    print(i)


num1 = 100
num2 = 20
add = num1 + num2
print('add=',add)
print('hello everyone')


numbers = [1, 2, 3, 4, 5]
second, *middle, last = numbers

print(second, end=",")   # 1
print(middle, end=",")  # [2, 3, 4]
print(last, end=",")
print('010','5966','6638', sep='-')   #end= 인수는 같은 줄에 결과가 출력되게끔 도와주는 것이다.

print("이름 : %s, 나이: %d, data = %.2f")

su = 5
dan = 800
print(id(su))
print(id(dan))
amount = dan * su
print(amount)

x = 2
y = x**2 * 2.5 + 3.3 * x + 6
print(y)
#
# fat = int(input("지방의 그램을 입력하세요 : "))
# carbohydrate = int(input("탄수화물의 그램을 입력하세요 : "))
# protein = int(input("단백질의 그램을 입력하세요 : "))
# total_cal = fat*9 + protein *4 + carbohydrate *4
# print(f"총칼로리 : {total_cal} cal")


# 삼항 조건문
# 변수 = 참 if (조건문) else 거짓
# import random
# print(random.choice([1,2,3,4,5,6]))
# a = [1,2,3,4, 5,6,7,8,9,11,21,12,13,14,15]
# print(random.choices(a,k=3))
# #여기서 k는 선택할 요소의 개수이다.
#
# latset = [1,2,3,4,5,6,7,8,9]
# for i in latset :
#     print('원소 :', i)
#
#
#
# for i in range(2,10):
#     print(f'~~~{i}단 ~~~')
#     for j in range(1,10):
#         print(f'{i} * {j} == {i*j}')


# chat_gpt = """아쉽게도 현재는 실시간으로 인터넷에서 정보를 가져올 수 없어서 과거의 특정 기사를 가져오기 어렵습니다.
# 하지만 특정 주제에 대한 정보나 질문에 답하는 데 도움을 드릴 수 있습니다. 다른 주제나 질문이 있으면 알려주세요!"""
#
# sents = []
# words = []
#
# sents_s = chat_gpt.split(sep='\n');
# words_s = chat_gpt.split()
# print(sents_s)
# print(words_s)


#항공사에서는 짐을 부칠 때, 10kg이상 부터 수수료를 내야한다. 수수료는 10의 배수 단위로 10,000원씩 증가한다. 만약 10kg 미만이염 수수료는 없다.
# 사용자의 짐의 무게를 키보드로 입력받고, 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하시오.

weight = int(input('당신의 수하물 무게는 얼마인가요?  : '))
def weight_extra_calc(kg):
    standard = kg // 10
    return f'당신이 지불하여야 하는 수수료는 {standard*10000}원 입니다.'

print(weight_extra_calc(weight))

import random
print('숫자 맞추기 게임')
com = random.randint(1,10) #1~10사이 난수 발생

while True:
    my = int(input('예상 숫자를 입력하시오 : '))
    if my == com:
        print('~~ 성공 ~~')
        break
    elif my < com:
        print('더 큰 수 입력')
    else:
        print('더 작은 수 입력.')


#1~100 사이에서 3의 배수이면서 2의 배수가 아닌 수를 한 줄에 출력하고, 누적합을 출력 하시오.
sum = 0
for i in range(1,100):
    if i % 3 == 0 and i % 2 != 0 :
        sum+=i
        print(sum)


multiline = """안녕하세요, 파이썬 세계로 오신걸 환영합니다. 파이썬은 비단뱀 처럼 매력적인 언어입니다."""
multiline_split = multiline.split()
print(multiline_split, len(multiline_split))
