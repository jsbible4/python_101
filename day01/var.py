# 변수(variable)

a = 100 # = 대입한다(오른쪽의 데이터 r-value를 왼쪽의 변수에 대입한다.-> 변수 선언한거임.
name = "정동하" # 문자를 쓰고 싶다면 무조건 ""더블쿼터를 사용해야 한다.
mbti = "intj"

print(a) #-> 이미 변수 선언 했기 때문에 "" 더블 쿼터 없어도 오류 안뜸.
print(name)
print(mbti)

# 변수 문법(규칙)
# 변수명은 문자, 숫자, 밑줄(_) 단, 숫자 시작은 불가
# 변수명은 대소문자 구분이 된다.
# 변수 국룰
# 1. 의미 있는 변수명
# 2. 소문자로 작성
# 3. 단어 + 단어: snake 방식, camel 방식 사용
# megastudy_python: snake 방식 (중간에 짝대기가 뱀이라고 생각)
# megastudyPython: camel 방식 (중간에 대문다가 낙타 홀 같아서)

newjeans_member = "하니"
newjeans_song = "ETA"

print(f"내가 좋아하는 뉴진스 멤버는 {newjeans_member}")  # 중괄호가 변수 처리됨. => f"{}"
print(f"내가 좋아하는 뉴진스 노래는 {newjeans_song}")

name1 = "이름" # 1name은 안됨.
