#조건부
a = ["짝" if i % 2 == 0 else "홀" for i in range(10)]
print(a)

b = ['🍕'if i%5 == 0 else '🌭'for i in range(1,100)]  # 1 부터 해야지 뒤집히지 않는다.
print(b)

#1~100 3의 배수이면 🍕 아니면 🍔
meal = [ '🍕' if i%3==0 else '🍔' for i in range(1,101)]
print(meal)



#중첩
# [값 for 변수1 in 반복가능객체1 for 변수2 in 반복가능객체2]
d = [i*j for i in range(1,10) for j in range(2,9)] # i j 서로 개수 안 맞으면 교집합되는 것 까지만 됨.
e = [i+j for i in 'abc' for j in '123'] #첫번째 a랑 1, 2, 3 ~~~
print(e)
# == ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
#온도를 화씨로 변환
celcius = input("지금은 섭씨로 몇도?:")
wendu = [(i*1.8)+32 for i in celcius]
print(wendu)