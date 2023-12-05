import random #random.을 쓰고 싶다면 import random 를 입력



player = ['손흥민','김민재','황희찬','이강인']
a = random.randint(0,10) # 0~10 중에 아무 정수를 랜덤으로 뽑아줘 #방법 1
b = random.choice(player) #방법2
# 0~10 정수 하나
print(a)
print(player[0])
print(b)

random.shuffle(player) #리스트 안을 섞는다.
print(player)

c = random.uniform(1.5,2.5) #  주어진 범위에서 무작위 실수
print(c)