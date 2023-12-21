# 일본 여행지 추가하기.
# 0. 여행 필수품 리스트 추가
# 1. 가는 곳 리스트 추가
# 2. 먹을 것 리스트 추가
# 3. 살 것 리스트 추가
# 4. 모든 리스트 보기
# 5. 프로그램 종료하기

def guide():
    print("""여행 계획 프로그램
    0. 여행 필수품
    1. 갈 곳 
    2. 먹을 것
    3. 살 것
    4. 모든 리스트 보여주기
    5. 종료
    """)
def necessity(list):   # list에 뭘 담으면 list가 출력됨.
    print(f"현재 리스트: {list}")
    item = input("추가할 리스트:")
    list.append(item)


while True:
    necessityList =[]
    placelist = []
    foodlist = []

    guide()
    systemCode = int(input("번호를 고르세요:"))
    if systemCode == 0:
        necessity(necessityList)





}
