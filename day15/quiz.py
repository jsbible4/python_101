# 1.제일 작은 수 제거하기
# 정수를 저장한 배열, arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수 solution을 완성해주세요
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
arr = [4,3,2,1]
def solution(arr):
    if len(arr) ==1:
        return -1
    else:
        minimum = min(arr)
        arr.remove(minimum)
        return arr

print(solution(arr))
print(solution([10]))

# 2. 문자열 섞기
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.
a = 'aaaaa'
b = 'bbbbb'
start = ''
for i in range(len(a)):
    start += a[i] + b[i]
print(start)

password = input('비번 입력: ')

if len(password) < 10:
    print('비번이 짧습니다.')
else:
    if not '!' in password or '@' in password or '#' in password:
        print('!@# 를 꼭 넣어주세요!')
    else:
        isAlphaOrNum = False
        for i in password:
            if i.isalnum():
                isAlphaOrNum = True
        if not isAlphaOrNum:
            print('영어 또는 숫자 포함하세요')
        else:
            print(f'비밀번호 완성입니다. 비밀번호는 : {password}')

##  ?????이거 진짜 이해가 넘 어렵디ㅏㅇ...ㅠㅠㅠㅠㅠㅠㅠㅠ눈물난당,ㅠ,ㅠㅠㅠ

