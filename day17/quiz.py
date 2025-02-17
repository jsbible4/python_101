# 1. 길이가 n이고, '수박수박수박수박수...'와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
string = '수박'

def solution(s):
    n = int(input('얼마나 반복할까요? (정수로 입력해주세요).'))
    if n % 2 == 0:
        empty_string = ''
        return empty_string + s * (n// 2)
    else:
        empty_string = ''
        return empty_string + s * (n//2) + s[0]
print(solution(string))


def water_melon(n):
    str = '수박'*n
    print(str)
    return str[:n]
n = int(input('얼마나 반복할까요? (정수로 입력해주세요).'))
print(water_melon(n))


# 2. 영어가 싫은 나운은 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록
# solution 함수를 완성해 주세요.
numbers = 'onetwothreefourfivesixseveneightnine'
numbers_list = ['one','two','three','four','five','six','seven','eight','nine']
def solution(n):
    for num, eng in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
        n = n.replace(eng,str(num))
    return int(n)

print(solution(numbers))


