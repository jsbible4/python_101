# 1. 리스트 컴프리헨션(리스트 데이터 조작)을 이용한 짝수 생성 (1~20)짝수만 포함하는 리스트 생성
a = [i for i in range(1,21) if i % 2 == 0]
print(a)

#2. 조건을 포함한 리스트 컴프리헨션
# 주어진 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 에서 5보다 큰 숫자만을 포함하는 새로운 리스트 생성
bigger = [i for i in range(1,11) if i > 5 ]
print(bigger)

# 3. 문자열 처리를 위한 리스트 컴프리헨션
# 문자열 리스트 ["apple", "banana", "cherry","date"]에서 각 단어의 첫 글자만을 추출하여 새로운 리스트 만들기
old_list = ["apple", "banana", "cherry","date"]
first_letter = [i[0] for i in old_list]
print(first_letter)

# 4. 중첩된 리스트 컴프리헨션
# 1 부터 5까지의 숫자를 포함하는 리스트 [1, 2, 3, 4, 5]를 사용하여 각 숫자의 제곱값을 포함하는 리스트 만들기
list = [1, 2, 3, 4, 5]
squared= [i**2 for i in list]
print(squared)

# 5. 문자열 길이 변환
# ["hello", "world", "python", "programming" ]에서 각 단어의 길이를 수하여 새로운 리스트를 만들기
string_list = ["hello", "world", "python", "programming" ]
length = [len(i) for i in string_list]
print(length)

# 6. 문자열 대문자 변환
# ["apple", "banana", "cherry"]의 각 단어를 대문자로 변환하여 새로운 리스트 만들기
string_list_2 = ["apple", "banana", "cherry"]
upper = [i.upper() for i in string_list_2]
print(upper)

# 7. 리스트 요소의 제곱
# 정수 리스트 [1, 3, 5, 7, 9]의 각 요소를 제곱하여 새로운 리스트 만들기.
int_list = [1, 3, 5, 7, 9]
multiple_int = [i**2 for i in int_list]
print(multiple_int)


