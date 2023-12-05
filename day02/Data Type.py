
#a = 1
#b = 1.5
# type()
# 해당 데이터의 타입을 알려줌.
#print(type("오늘 기분이 그냥 그럼"))  #type(a)는 정수. 어떤 데이터 타입을 출력해줘 해서 나타남.

a = int(input("숫자 하나를 입력하세요."))
b = int(input("숫자 하나 더 입력하세요."))
print(type(a))
print(type(b))
# a b 를 숫자로 인식한게 아니라 문자로 인식했기 때문이다.
#add = int(a)+int(b)
print(f"두 수의 합은 {a+b}입니다.")

#int()    # 정수화 시켜주는 함수
#a = int("1")
#b = int("12")
#print(f"{a+b}")  # 정수화시켰기때문에 112가 아니라 13이 나옴/.