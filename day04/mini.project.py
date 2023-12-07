#유저한테 해당 범위를 지정받습니다.
#랜덤 숫자를 뽑습니다
#유저가 랜덤 숫자가 뭔지 맞춥니다.
# 맞으면 맞습니다. 아니면 틀렸습니다. 로 하십시오ㅓ
import random

a = int(input("아무 자연수나 골라주세요."))

pick = random.randint(1,a)
test = int(input("랜덤으로 나온 자연수를 맞춰보세요!")) ##input 자체가 출력 함수의 역할을 하기 때문에 굳이 print 함수를 사용할 필요가 없다.
print("맞습니다" if pick == test else "틀렸습니다. retry 하세요.")