
import random

#양의 정수를 입력 받아 시:분:초 형태로 출력하는 프로그램
a = int(input("양의 정수를 입력해주세요."))
print(f"양의 정수는  {a//3600} :  {(a% 3600) //60}  : {a% 60} 로 출력됩니다.")
#계산하는 연산 영역은 {} 안에 들어가야 한다.

# 뉴스 기사 단어 별로 정렬화 퀴즈
news = """Test-takers of South Korea’s national college entrance exam, known as the Suneung, 
are set to receive their test results Friday, amid lingering controversy over whether this year's 
test succeeded in completely scrapping the highly difficult “killer questions.”

Results and analysis of over 440,000 examinees released by the Korea Institute for Curriculum and Evaluation on
Thursday suggested that exams in all subjects, including Korean language, mathematics and English, were more challenging than last year, especially for top test-takers."""

a = news.split()

a.sort() #리스트 안에서 믹싱 하는 거는 변수화 시켜주지 않는다.
print(a)

# 점심 메뉴 추천(점메추) 프로그램

main_dish = ['🍘', '🍚', '🍲', '🍳', '🍛']
dessert = ['🍹', '☕', '🍪', '🥨', '🍬']
drinks = ['아아', '라떼', '스무디', '쿠키앤크림', '과일주스']


print(f"메인 음식 : {random.choice(main_dish)}, 후식 : {random.choice(dessert)}, 음료 : {random.choice(drinks)}")

