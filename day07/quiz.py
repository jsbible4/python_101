#x, y 값을 입력받고, 해당 좌표의 위치하는 분면을 출력하는 프로그램
x = float(input("x의 값을 입력하시오"))
y = float(input("y의 값을 입력하시오"))
if x>0 and y>0:
    print("1사분면")
elif x<0 and y>0:
    print("2사분면")
elif x<0 and y<0:
    print("3사분면")
elif x or y == 0:
    print("") #x, y 축 위에 존재, 원점 ~~
else:
    print("4사분면")

#사용자로부터 음료의 종류를 나타내는 정수 1~3과 투입한 금액을 나타내는 양의 정수를 입력받는다.
#사용자가 선택한 음료의 이름과 투입한 금액에서 음료 가격을 뺀 잔돈을 출력하는 프로그램 작성.

beverage = int(input("음료수를 선택해주세요."))
cost = int(input("투입할 금액을 알려주세요."))
change = {
    1 : {
        "name" : "아메리카노",
        "cash":3000
    },
    2 : {
        "name" : "레몬에이드",
        "cash" : 4000
    },
    3 : {
        "name" : "라떼",
        "cash" : 3500
    },
}
print(f"귀하가 고르신 음료는 {change[beverage]['name']}이고 잔돈은 {cost - change[beverage]['cash']}입니다.")  #변수 인용 할 때 문자열 안에서 인용한다면 문자와 구분해주기 위해 {}중괄호를 사용한다.
# 문자열 안에서의 ㅇ인용이 아니니까 변수사용할 때 {}중괄호 사용하지 않아도 됨.

#간단한 퀴즈 프로그램 만들기
#사용자가 질문에 답변하고, 정답 여부를 확인할 수 있는 간단한 퀴즈 프로그램을 파이썬으로 작성.
#1. 각 질문과 그에 대한 정답을 저장하는 딕셔너리
#2. 사용자에게 질문을 하나씩 보여주고, 답변을 입력받는다.
#3. 사용자의 답변이 정답과 일치하는지 확인. 정답이면 정답입니다. 틀렸으면 틀렸습니다. 정답은 [정답]입니다. 출력
# 모든 질문에 ㄷㅂ한 후, 사용자가 얻은 총 점수를 보여준다.

quizzes = {
    1:{
        "question1": "정동하는 몇살입니까?(윤석열 나이로)",
        "answer" : "18"
    },
    2:{
        "question2": "정동하가 다니고 있는 메가스터디 IT 아카데미는 지하철 몇 호선 근처에 있습니까?(가장 가까운 역 기준)",
        "answer" : "2"
    },
    3: {
        "question3": "신체적으로 건강한 인간이라면 손가락은 몇개를 가지고 있습니까?",
        "answer" : "10"
    }
}


points = 0  #초기값 설정

print(quizzes[1]["question1"])
answer = input("정답 입력:")  # 답이 정수면 int, 문자열이면 문자열에 맞춰서 설정해준다.
if answer == quizzes[1]["answer"]:
    print("정답입니다.")
    points+= 1
else:
    print("틀렸습니다. 정답은 [18]입니다.")


print(quizzes[2]["question2"])
answer = input("정답 입력:")
if answer == quizzes[2]["answer"]:
    print("정답입니다.")
    points += 1
else:
    print("틀렸습니다. 정답은 [2]입니다.")


print(quizzes[3]["question3"])
answer = input("정답 입력:")
if answer == quizzes[3]["answer"]:
    print("정답입니다.")
    points += 1
else:
    print("틀렸습니다. 정답은 [10]입니다.")

print(f"맞춘 개수는 {points}/3개 입니다.")

