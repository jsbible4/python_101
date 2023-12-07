#유저한테 해당 범위를 지정 받습니다. 1~n
#n의 범위를 지정해주세요! 라고 입력을 받는다.
# 1~n 어떤 정수를 임의로 뽑히고
# 맞는다면 맞습니다! 축하드립니다! 라고 멘트가 나와야 하고,
# 틀리면 틀렸습니다. 다시 한번 맞춰보세요
import random
a = int(input("n의 범위를 지정해주세요!"))
pick = random.randint(1,a)
target = int(input("해당 랜덤 숫자를 맞춰보세요!"))
msg = "맞는다면 맞습니다! 축하드립니다!" if pick == target else "틀렸습니다."
print(msg)




