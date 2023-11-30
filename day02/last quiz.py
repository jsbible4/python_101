# 태어난 년도 입력하고 현재 만나이 출력
# birth = int(input("태어난 년도는?"))
# current_year = int(input("올해는 몇년도?"))
# print(f"만나이는 {current_year-birth}")

# 세 개의 숫자 평균 계산기
# a = int(input("숫자 하나를 입력하시오."))
# b = int(input("숫자 하나를 입력하시오."))
# c = int(input("숫자 하나를 입력하시오."))
# print(f"세 수의 평균은 {(a+b+c)/3}")

# 환율 계산기
# won = int(input("원을 입력하세요"))
# print(f"엔화로는{113.73*1000/won}엔 달러화는 {0.77*1000/won}달러 입니다. ")

#거리 변환기
# a = float(input("1km 당 몇 mile 인가?"))
# b = int(input("몇 km인가?"))
# print(f"{b}km는 {a*b}mile 이다.")

# 체온 변환기
# C = int(input("지금 섭씨 온도는 몇 C인가?"))
# print(f"섭씨 온도 {a}는 화씨 온도 {C*59+32}이다.")

# 체질량 지수(BMI) 계산기
# a = int(input("당신의 키는?"))
# b = int(input("당신의 몸무게는?"))
# print(f"당신의 체질량 지수(BMI)는 {b/a**2}") #**제곱 표시를 의미함.

# 여행 시간 계산기
# a = int(input("여행할 거리는?"))
# b = int(input("평균 이동 속도는?"))
# print(f"도착까지 걸리는 시간은 {a/b}시간")


# 반지름을 입력 받을 때 원의 둘레를 출력하는 프로그램
radius = int(input("반지름의 길이를 입력하시오"))
print(f"원의 둘레는 {radius*2}파이이다.")

# 반지름을 입력 받을 떄 원의 넓이를 출력하는 프로그램
radius2 = int(input("반지름의 길이를 입력하시오"))
print(f"원의 넚이는 {radius**2}파이이다.")

# 반지름을 입력 받을 떄 구의 부피를 출력하는 프로그램
radius3 = int(input("반지름의 길이를 입력하시오"))
print(f"구의 부피는 {(4/3)*(radius**3)}파이이다.")

# 한 변의 길이를 입력하고 정사각형의 둘레와 넓이를 출력하는 프로그램
side = int(input("정사각형의 한 변의 길이를 입력하시오."))
print(f"정사각형의 둘레는 {side*4}이고, 넓이는 {side**2}이다.")
