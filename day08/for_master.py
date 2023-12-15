#1자리 숫자의 합 구하기
#"정수 n이 주어질 떄, n의 각 자리 숫자의 합을 계산해보세요!"
number = (input("아무 자연수를 적어주세요!"))
sum = 0
for i in number:   #문자열, 리스트만 들어갈 수 있기 때문에 number 부터 int 시켜주면 안 된다.
    sum += int(i)
print(sum)

# 배수만 골라내기
#"정수 n과 정수 배열 numlist 가 주어졌을 때, numlist에서 n의 배수가 아닌 수들을 제거한 후 그 배열을 반환하시오."
numlist = [ 3, 5, 7, 8, 4, 15, 27, 35, 55]
n = 8
a = [i for i in numlist if i % n == 0]
print(a)

#대소문자 바꾸기
#문자열 my_string이 주어질 떄, 대문자는 소문자로, 소문자는 대문자로 변환한 문자열을 반환하세요!
my_string = input("문자열 아무거나 쓰세요!")
for i in my_string:
    if i.isupper():
        print(i.lower())
    else:
        print(i.upper())


# 특정 숫자의 자리 수 찾기
#"정수 num과 k 가 주어질 때, num을 이루는 숫자 중에 k가 있으면 num에서 그 숫자가 있는 자리수를 반환하고, 없으면 -1을 반환하세요!"
num = input("아무 정수를 입력해줘.")
find = input("찾고 싶은 숫자 입력")
isFind = False
for index, number in enumerate(num):
    if number == find:
        print(index + 1)
        isFind = True
        break
if isFind == False:
    print(-1)