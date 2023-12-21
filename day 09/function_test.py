# 중복되는 행동 매일 해야하는가?
# 자동화 시켜주는게 함수

# 함수 모양: ~~~()

# 출국 시간, 도착 시간
# 이 비행기는 출국 시간: ~~ 도착 시간: ~~ 비행기입니다.

def time(a,b):
    print(f"이 비행기는 출국 시간: {a} 도착 시간: {b} 비행기 입니다.")

time('10','13:10')


# 과일 리스트를 두 개 받고, 두 리스트를 합쳐서 뱉는다.

def mix_fruits(fruit1, fruit2):
    return [i+j for i in fruit1 for j in fruit2]
a = mix_fruits(['🍉','🍋','🍌','🍍'],['🥭','🍎','🍏','🍐'])
print(a)