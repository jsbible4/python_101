#비교연산자
a = 10
b = 20
# 동등 비교
print(f"{a} = {b} : {a==b}")
print(f"{a>b}")
# 부등 비교
print(f"{a}!={b} : {a!=b}")
#보다 큼 비교
print(f"{a} > {b}: {a>b}")
#보다 작음 비교
print(f"{a}<{b}: {a<b}")
#보다 크거나 같음 비교
print(f"{a}>={b}:{a>=b}")
#보다 작거나 같음 비교
print(f"{a}<={b}: {a<=b}")


#or, and,... 논리 연산자
c = 3 > 1 or 5 < 1 # or 하나라도 True이면 True(합집합 개념)
d = 3>1 and 5<1 #and 하나라도 False 이면 False

e =  not (3 > 1 or 5 < 1)
print(e)  #답이 반대로 나온다.

#할당 연산자

f = 1 #1 할당한거임

# == (같다), =(왼쪽의 값을 오른쪽 변수에 넣는다[할당])
f = f + 100 # 101
f +=100 # 101 축약형

