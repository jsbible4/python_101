# 5명씩
# 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서 있는 사람들의 이름이 담긴 문자열 리스트 names 가 주어질 때, 앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서 있는
# 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성해주세요. 마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.

names = ['nami','ahri','jayce','garen','ivern','vex','jinx']
def solution(list):
    return [e for i,e in enumerate(list) if i % 5 == 1]
print(solution(names))

#ad 제거하기
# 문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 'ad'라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로
#return 하는 solution 함수를 완성해 주세요.
strArr = ['and','notad','abcd']
def solution(list):
    return [i for i in list if not 'ad' in i]
print(solution(strArr))

strArr2 = ['there','are','no','a','ds']
def solution2(list):
    return [i for i in list if not 'ad' in i]
print(solution2(strArr2))


# 3. 한 번만 등장한 문자
# 문자열 s가 매개변수로 주어진다. s 에서 한 번만 등장하는 문자를 사전 순(오름차순)으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
string = 'abdc'
# ss = 'abdc'
string_list = list(string)
string_list.sort()
string_list2 = [i for i in string_list if string_list.count(i) == 1]
emptyWord = ''
for i in string_list2:
    emptyWord += i
print(emptyWord)


