# 유저한테 과일 이모지 다섯개를 입력받고
# 랜덤으로 해당 과일을 뽑아서
#~~과일은 맛있죠!
import random
fruits = []  #빈 리스트를

five_fruits = input("과일 입력해줘.")
fruits.append(five_fruits)

five_fruits = input("과일 입력해줘.")
fruits.append(five_fruits)

five_fruits = input("과일 입력해줘.")
fruits.append(five_fruits)

five_fruits = input("과일 입력해줘.")
fruits.append(five_fruits)

five_fruits = input("과일 입력해줘.")
fruits.append(five_fruits)

b = random.choice(fruits)
print(f"{b}가 참 맛있죠!")


