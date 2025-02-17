# 문자열 strArr이 주어진다. strAtrr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return하는 solution 함수를 완성해주세요.
strArr = ['a', 'bc', 'd', 'efg', 'hi', ' g']
# length = []
# count = 0
# for i in strArr:
#     length.append(len(i))
#     length.sort()
#
# print(length)
#
# for i in length:
#     length_counted = length.count(i)
#     if count <= length_counted:
#         count = length_counted
# print(count)

def solution(strArr):
    length_count = {}
    for i in strArr:
        length = len(i)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1  # 키 값이 없어도 이렇게 갱신시킬 수 있다.
            print(length_count)
    return max(length_count.values())
print(solution(strArr))

# 2. 369 게임.
# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,21,23,26,99]
# for i in num:
#     if i <= 10 and i % 3 == 0 :
#         print('👏')
#     elif i > 10:
#         first = i // 10
#         if (i - first) % 3 == 0:
#             print('👏')
#         else:
#             print(i)
#     else:
#         print(i)
# 이렇게 하면 첫째자리가 3 6 9 중 하나인 게 박수로 나오지 않는다.
def clapping():
    for i in range(1,101):
        if str(i % 10) in '369' or str(i // 10) in '369':
            if str(i % 10) in '369' and str(i // 10) in '369':
                print('👏👏')
            else:
                print('👏')
        else:
            print(i)

    # return ['👏' if str(i % 10) in '369' or str(i // 10) in '369' else i for i in range(1, 101)]
print(clapping())
