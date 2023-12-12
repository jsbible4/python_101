#d = set([1,2,3,4,5,1,2,3,4,5,5,5])
#print(d)

#food ={1,2,3,4,5}
#food.add("붕어빵")
#food.add("latte")
#food.add(5)
#print(food)

#lunch = {"ramen", "pizza", "pasta", "sandwich"}
#dinner = {"pizza","sandwich", "none", "latte"}
#lunch.update(dinner) #lunch, dinner 집합을 합집합 시키는 것. = update
#print(lunch)

# 제거 함수 remove or discard
dinner = {"pizza","sandwich", "none", "latte"}
#dinner.remove("none") # 없는것을 뺴면 에러남
#dinner.discard("latte") # 없는 것을 빼도 에러 안남/-> 엥간하면 discard 를 쓰자!

#랜덤 제거 함수 pop
#dinner.pop() #아무거나 빼줌.

#모두 제거 함수 clear
#dinner.clear()
#print(dinner)

#세트의 수학적 연산
nation = {"Swiss", "Japan","Thailand", "France" }
europe = {"Swiss", "France", "England", "Germany"}

#합집합
uni = nation.union(europe)
print(uni)

#교집합
inter = nation.intersection(europe)
print(inter)

#차집합
diff = nation.difference(europe)
print(diff)

# 대칭 차집합
symmetric = nation.symmetric_difference(europe)
print(symmetric)