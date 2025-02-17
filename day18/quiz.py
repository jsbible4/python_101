# 1. 제일 작은 수 제거하기
# 정수를 저장한 배열, arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        minimum = min(arr)
        arr.remove(minimum)
        return arr
arr = [4,3,2,1]
arr2 = [10]
print(solution(arr))
print(solution(arr2))

# 2. 문자열 섞기
# 문자열 my_str 과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution함수를 완성해주세요.
my_str = 'abc1Addfggg4556b'
n = 6


def main_solution(my_str,n):
    empty = []
    for i in range(0,len(my_str),n): #0부터 문자열 my_str의 길이까지 n 간격으로 순회하면서, 각 순회에서 i에는 현재 순회 중인 범위의 시작 인덱스가 할당됨.
        empty.append(my_str[i:i+n])
    return empty

print(main_solution(my_str,5))
