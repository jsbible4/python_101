# 1. 리스트 컴프리헨션 필터링
words = ["apple", "banana", "cherry","date", "elderberry", "fig"]
aa = [i for i in words if len(i)>=5 and "a" in i]
print(aa)


# 2. 리스트 컴프리헨션 필터링 (숫자)
a = [i for i in [30, 55, 20, 75, 40, 90, 10, 65] if i > 50 ]
print(a)

# 3. 리스트 컴프리헨션(문자열 조합)
# 주어진 두 개의 리스트에서 가능한 모든 문자열 조합을 생성하는 리스트 컴프리헨션 작성.
def mix_string(string1, string2):
    return [i+j for i in string1 for j in string2]
a = mix_string(['a','b','c'],['x','y','z'])
print(a)

#4. 리스트 컴프리헨션(두 리스트의 합)
# 두 개의 동일한 길이를 가진 리스트를 받아 각 리스트의 요소를 더한 결과 리스트를 생성하는 리스트 컴프리헨션을 작성.
a = [i+j for i in [1, 2, 3, 4, 5] for j in [10, 20, 30, 40, 50]]
print(a)

# 5. 리스트 컴프리헨션(짝수의 제곱)
# 1부터 10까지의 자연수 중에서 짝수의 제곱으로 이루어진 리스트를 생성하는 리스트 컴프리헨션을 작성.
a = [i**2 for i in range(1,11) if i % 2 == 0 ]
print(a)


# 6. 가장 작은 5개의 수 제외한 수들
# 정수로 이루어진 리스트 num_list가 주어진다.
#num_list 에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 반화하는 solution1 함수를 완성

#프로그래밍에서 변수를 immutable
#변수안에 있는 내용을 엥간하면 바꾸지 말자는 대원칙을 지향함.
#왜? 헷갈리니까

def solution1(num_list):
    num_list.sort()   #[1, 2, 3, 4, 5] 정렬 = 순서 배치만 바꾼거임. 내용을 바꾼게 아님.
    result = num_list[5:]   # 자르거나 없애거나 하는 것은 새로운 변수에 담는 편이 좋다.
    return result   # return이 있어야 무조건 함수를 다시 부를 때 뜬다. 없으면 저장됐다가 바로 삭제라서 우리 눈에 안 보임.

# 7.
def solution2(a,b,flag):
    if flag:
        print(a + b)
    else:
        print(a - b)

# 8.
def solution3(start_num, end_num):
    result = [i for i in range(start_num, end_num+1)]
    return result



