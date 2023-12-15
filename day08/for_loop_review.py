#1. for-range
for i in range(0,100):
    print(f"{i}, fnlol")
#2. for - list or str
coin = ['비트코인', '이더리움', '리플', '에이다']
for i in coin:
    print(i)

sign = "비트코인 떡상"
for i in sign:
    print(i)

# 3. for i in enumerate(list or str)
for index, name in enumerate(coin):
    print(index, name)

arr = [3,1,23,5,13,45,15]
sum = 0
for i in arr:
    sum += i

print(f"리스트의 모든 값의 평균은 {sum/len(arr)}입니다.")

import random
n = int(input("n은 무슨 자연수입니까?"))
list = []
total = 0

for i in range(n):
    a = random.randint(0,10000)
    list.append(a)
    total = total + a
print(f"배열의 평균은 {total/len(list)}")