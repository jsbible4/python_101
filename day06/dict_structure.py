capital = {
    "korea" : "seoul",
    "china" : "beijing",
    "malaysia" : "kuala lumpur",
    "USA" : "washington DC"
}

print(capital["korea"]) #[]dict 에 해당하는 약속
# 왼쪽에는 핵심 단어, 오른쪽은 왼쪽에 상응하는 단어(아무 data type이 들어와도 된다.)
pizza_price = {
    "sweetpotato_pizza": 17000,
    "pepperoni_pizza": 14000,
    "hawaiian_pizza": 18000,
    "bulgogi_pizza": 15000
}
print(pizza_price["hawaiian_pizza"])

japan_travel = {
    "동하":['온천여행', '눈싸움'],
    "나은":['초밥', '기모노'],
    "유진":['맛집', '디즈니랜드'],
    "동준":['당고', '도쿄타워']
}
print(japan_travel["나은"])  #오른쪽에는 어떤 data type 도 올 수 있다는 말.

usa_travel = {
    "동하":{
        "항공": "대한항공",
        "가고 싶은 곳": "뉴욕",
        "먹고 싶은 것": "햄버거"
    },
    "유진":{
        "항공": "제주항공",
        "가고 싶은 곳": "로스앤젤러스",
        "먹고 싶은 것": "피자"
    }
}
print(usa_travel["동하"])
print(usa_travel["동하"]["먹고 싶은 것"])  #dict 안에 dict 예시

