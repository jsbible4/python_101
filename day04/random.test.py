import random #random.을 쓰고 싶다면 import random 를 입력



player = ['손흥민','김민재','황희찬','이강인']
# 0~10 중에 아무 정수를 랜덤으로 뽑아줘 #방법 1

b = random.choice(player) #방법2
# 0~10 정수 하나
print(random.randint(0,10))
print(player[0])
print(b)

random.shuffle(player) #리스트 안을 섞는다.
print(player)

c = random.uniform(1.5,2.5) #  주어진 범위에서 무작위 실수
print(c)

#기사를 어절 별 리스트화 시키고 맨 앞에 Esther 를 추가 한 뒤
#리스트 안에서 랜덤으로 뽑는다.

news = """Hyundai Motor Group Executive Chair Chung Euisun on Friday reiterated the automaker’s unwavering support for Korean archery, emphasizing the need to find ways for archery to contribute to the society.

“In the mid to long term, (we) should put in effort to (bring archery) closer to the public and we must think about how archery can contribute to our society and act on it,” 

said Chung at an event held at Grand Walkerhill Seoul to commemorate the 60th anniversary of South Korean archery.

“Based on the principles of fairness and transparency, the Korean Archery Association will be at the forefront of innovation, 

receive trust and love from the people and serve an appropriate social role."""

b = news.split()
print(b)   #split 자체가 찢어서 리스트 안에 넣는다 이기 때문에 따로 list 안에 담아주는 과정이 필요없다.
b.append("Esther")
print(b)
import random

print(random.choice(b))

print(random.uniform(0,10))
random.shuffle(b)  #이거 할 때 변수 붙이지 않는 이유는??? ==list 조작이기 때문에
print(b)
