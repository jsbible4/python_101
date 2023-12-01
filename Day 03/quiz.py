# 원을 입력 받고 위안화로 바꿔주는 프로그램
won = int(input("won을 입력하시오."))
print(f"{won}은 중국 돈으로 {0.0055*won}")
# 0.54/won*1000
# 원을 입력 받고 유로화로 바꿔주는 프로그램
won = int(input("won을 입력하시오."))
print(f"{won}은 유로로 {0.0007*won}")

# 한 변의 길이와 높이를 받아 정삼각형 넓이 구하는 프로그램
side = float(input("한 변의 길이는?"))
height = float(input("정삼각형의 높이는?"))
print(f"정삼각형의 넓이는 {side*height*0.5}")

#시간 단위인 초를 입력 받으면 분으로 바꾸는 프로그램
second = int(input("몇 초 인가?"))
print(f"{second}초는 {second/60}분이다.")
# num //분, % 초 이다. (몫과 나머지를 나누는 방법도 있음. )


#a, b, c를 입력받아 이차방정식의 양의 해를 도출하는 프로그램(실근이 존재할 경우만)
a = int(input("아무 자연수를 쓰시오."))
b = int(input("아무 자연수를 쓰시오."))
c = int(input("아무 자연수를 쓰시오."))
print(f" {a}x**2 + {b}x + {c} = 0 에서 x는 {b**2}")  #루트 어떻게 쓸 지 몰라서 패스~~