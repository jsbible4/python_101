# mbti
#당신의 mbti를 입력하세요: INTJ
#당신은 내향적이고 직관적이며 이성적이고 계획적이시군요.

personality = input("당신의 mbti는??")
mbti = {
    "E" : "외향적",  #쉼표가 구분해줌.
    "I" : "내향적",
    "S" : "감각적",
    "N" : "직관적",
    "T" : "이성적",
    "F" : "감정적",
    "P" : "즉흥적",
    "J" : "계획적"
}
print(mbti[personality[0]]+mbti[personality[1]]+mbti[personality[2]]+mbti[personality[3]])