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



