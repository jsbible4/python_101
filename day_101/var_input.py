#input은 콘솔에 유저가 입력한 값을 받는 함수
# print("뉴진스 짱짱")
# input("뉴진스 중에 좋아하는 노래 뭐임?")  #그리고 콘솔에 유저가 답변을 입력 "하입보이" 유저가 값을 입력할 떄까지 기다리는 것이다. 유저가 입력한 값에 따라서 변수가 바뀌는 것이다.

#newjeans_song = input("뉴진스 중에 좋아하는 노래 뭐임?")
#print(f"너가 좋아하는 뉴진스 노래는 {newjeans_song}이구나")
#bangtan_song = input("방탄 노래 중에 좋아하는 거 뭐임?")
#print(f"너가 좋아하는 방탄 노래는 {bangtan_song}이구나")
your_name = input("당신의 이름은 무엇입니까?")
age = input("당신은 몇살입니까?")
first = input("외향입니까? 내향입니까?(E 또는 I 입력)") #유저가 답하기 쉽게 (E 또는 I 입력)
second = input("직관적입니까? 감각적입니까?(N 또는 S 입력)")
third = input("감성적입니까? 이성적입니까? (F 또는 T 입력)")
fourth = input("즉흥적입니까? 계획적입니까? (P 또는 J 입력)")
print(f"{your_name}는 {age}세이고 mbti는 {first}{second}{third}{fourth}")



