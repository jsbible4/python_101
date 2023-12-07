#x = 5
#if x > 0:   #:를 붙여줘야 한다.
    #print("양수 입니다. ")
#elif x == 0:#3가지 이상의 케이스 나타낼 때
    #print("0 입니다. ")

#else:  #모든 위에 있는 경우의 수를 제외한 나머지.
    #print("음수 입니다.")

#score = int(input("당신의 점수를 입력해주세요."))
#if score == 100:
    #print("축하합니다. 만점입니다.")
#elif 100>score and score>=70:   #and 로 하면 정석 # 직관적으로는 100>score>=70도 됨.
    #print("잘하셨습니다.")
#else:     #모든 위에 있는 경우의 수를 제외한 나머지.
    #print("열공하세요~")


    # 양의 홀수? 양의 짝수? 음의 홀수인지, 음의 짝수인지, 아니면 0 인지 확인해보는 프로그램 만들기
#number = int(input("아무 정수를 입력하시오./"))
#if number>0:
    #if number%2 == 0:
        #print("양의 짝수입니다.")
    #else:
        #print("양의 홀수입니다.")
#elif number<0:
    #if number%2 == 0:
        #print("음의 짝수입니다.")
    #else:
        #print("음의 홀수입니다.")
#else:
    #print("0 입니다. ")


#알파벳 탐지기
#"안녕하세요, 문자 한 개를 입력해주세요! 만약 알파벳이라면 '알파벳입니다!' 를 아니면 '알파벳이 아닙니다'

letter = input("문자 한 개를 입력해주세요!")
if letter.isalpha(): #str.isalpha  :  letter 가 알파벳이 맞는지 아닌지, 문자들(영어, 한글 등등 모든 문자) 다 포함을 확인해주는 문자열 함수
    print("알파벳입니다!")
else:
    print("알파벳이 아닙니다!")


# 비밀번호 유효 타입 체크
# 비밀번호를 입력을 받고
# 비밀번호의 시작이 영어 알파벳 대문자로 시작하면
# 비밀번호를 옳게 설정했습니다.
# 아니면 비밀번호 첫글자는 대문자로 설정해주세요!

#password = input("비밀번호를 입력해주세요!")
#if password.startswith('A'or'E'): # 아니면 password[0] == 'A' or 'B'도 가능
    #print("비밀번호를 옳게 설정했습니다!")
#else:
    #print("비밀번호 첫글자는 대문자 A or E로 설정해주세요!")

password = input("비밀번호를 입력해주세요!")

if password[0].isupper():
        print("비밀번호를 옳게 설정했습니다!")
elif len(password)<=8:
    print("비밀번호를 8글자 이상으로 해주세요!")
elif password.isalpha():
    print('비밀번호에 특수문자를 넣어주세요')
else:
    print('잘 설정하셨습니다.')



