# 영어 점수, 등급 매기기
grade = int(input("0부터 100 사이의 영어 점수를 입력해보세요!"))
if grade < 60:
    print("아쉽게도 탈락입니다 ㅠ")
elif 100>=grade>=90:
    print("A")
elif 90>grade>=80:
    print('B')
elif 80> grade >=70:
    print('C')
else:
    print('D')

#각도의 비밀을 밝혀라
# 각도를 입력해주세요!
#예각이면 1, 직각이면 2, 둔각이면 3, 평각이면 4로 분류해서 알려드릴게요!

angle = int(input("각도를 입력해주세요!"))
if angle == 90:
    print('2 : 직각입니다.')
elif angle < 90:
    print('1 : 예각입니다.')
elif angle>90 and angle % 180 != 0:
    print('3 : 둔각입니다.')
else:
    print('4: 평각입니다.')

# 대소문자 바꾸기
#문자열을 입력하면, 대문자는 소문자로, 소문자는 대문자로 바꿔드릴게요!
str = input("문자열을 입력하세요!")
if str.isupper():
    print(str.lower())
else:
    print(str.upper())

# 점수에 따른 등급과 피드백
# 국어, 영어 수학 점수를 입력해주세요. 평균 점수에 따라 A, B, C 등급을 매겨드리고,
#만약 한 과목이 100점이면 'GOOD', 60점 이하면 'BAD'라고 알려드릴게요!

mother_language = int(input("국어 점수를 입력해주세요"))
math = int(input("수학 점수를 입력해주세요"))
english = int(input("영어 점수를 입력해주세요"))
if 100>(mother_language + math + english)//3>=90:
    print("A")
elif 90>(mother_language + math + english)//3>=80:
    print("B")
else:
    print("c")

if mother_language or math or english == 100:
    print("GOOD")
else:
    print("")

if mother_language or math or english <= 60:
    print("BAD")
else:
    print("")



# 영화 티켓 예매 시스템

