#1. 홀짝에 따라 다른 값 반환하기
#양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return하고, n이 짝수라면 n이하의 짝수인 모든 양의 정수의 제곱의 합을 return
#하는 solution 함수를 작성해 주자.

def solution(n):
    empty = 0
    if n % 2 == 1:
        for i in range(1,n+1,2):
            empty += i
    else:
        for i in range(2,n+1,2):
            empty += i**2
    return empty

n = int(input("아무 양의 정수 하나를 입력해주세요."))
print(solution(n))

from functools import reduce
# reduce(lambda x,y:x+y,numbers)
def solution(n):
    if n % 2 == 1:  # reduce()누적함수
        return reduce(lambda x,y : x+y , range(1,n+1,2))
    else:
        return reduce(lambda x,y : x+y**2 , range(0,n+1,2))   # 추가되는 y를 제곱해서 누적해준다. x는 기존의 수.
print(solution(6))

#특정 문자열 리스트에서 특정 문자로 시작하는 단어만 필터링하여 반환하는 함수를 작성하세요. filter 함수를 사용하세요.

def filter_words_starting_with(words, start_char):
    filtered_words = list(filter(lambda words: words.startswith(start_char),words))
    return filtered_words

words = ['apple', 'banana', 'apricot', 'cherry']
start_char = 'a'


print(filter_words_starting_with(['apple', 'banana', 'apricot', 'cherry'], 'a'))


# 3. x 사이의 개수
# 문자열이 주어진다. 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return .
string = "oxooxoxxox"
string2 = "xabcxdefxghi"
a = string.split('x')  #x를 기준으로 분할에서 리스트에 담기
no_x = list(filter(lambda x: len(x) > 0,a))
mapped = list(map(lambda x: len(x),no_x))
print(no_x)
print(mapped)

# 더 작게 만들기
def xFilter(n):
    return list(map(lambda x: len(x),list(filter(lambda x: len(x) > 0,n.split('x')))))
print(xFilter("oxooxoxxox"))

