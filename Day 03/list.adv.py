news = """Hyundai Motor Group Executive Chair Chung Euisun on Friday reiterated the automaker’s unwavering support for Korean archery, emphasizing the need to find ways for archery to contribute to the society.

“In the mid to long term, (we) should put in effort to (bring archery) closer to the public and we must think about how archery can contribute to our society and act on it,” 

said Chung at an event held at Grand Walkerhill Seoul to commemorate the 60th anniversary of South Korean archery.

“Based on the principles of fairness and transparency, the Korean Archery Association will be at the forefront of innovation, 

receive trust and love from the people and serve an appropriate social role.”"""


print(f"to라는 단어는 뉴스에서 {news.count('to')}개 있습니다.")
# list 안의 단어를 바꾸는 거는 print 안에{}에서 바로 append 같은 거를 하면 안됨
# ex) coffee = ['a', 'b', 'c']
# coffee.append(d)
# print(f"너가 좋아하는 커피 리스트는 {coffee}구나.")
# 근데 그냥 list 안에서 무언가를 찾는 것은 print 안에{}에서 바로 count 해도 됨.


#단어별로 리스트화
#오름차순 정리
a = """Hyundai Motor Group Executive Chair Chung Euisun on Friday reiterated the automaker’s unwavering support for Korean archery, emphasizing the need to find ways for archery to contribute to the society.

“In the mid to long term, (we) should put in effort to (bring archery) closer to the public and we must think about how archery can contribute to our society and act on it,” 

said Chung at an event held at Grand Walkerhill Seoul to commemorate the 60th anniversary of South Korean archery.

“Based on the principles of fairness and transparency, the Korean Archery Association will be at the forefront of innovation, 

receive trust and love from the people and serve an appropriate social role."""

b = a.split()
b.sort()   #data type이 변하는 경우 변수에 넣어주는 걸 대원칙으로 한다.
print(b) #조작하는 거라서 b.sort() 따로 분리해서 써줘야 한다.


