for i in range(1000):
    if i ==250:
        break
    print(i)


#for 문 컴프리헨젼
#컴프리헨젼을 쓰면 보다 쉽게 데이터 정리가능
for i in range(1000):
    [].append(i)
# [표현식 for 미지수 in 리스트, 문자열, range(n) if 조건문]
a = [i for i in range(10)]
print(a)

#표현식은 말 그래도 어떻게 표현하고 싶은지를 나타냄.
arr = [x for x in range(100) if x % 5 ==0]  #5의 배수만 나오게
print(arr)

arrr = [ x**2 for x in range(100)]
print(arr)

arrrr = [x+10 for x in range(100) if x % 10 == 0]   #  != ~을 제외한이 된다.
print(arrrr)

lengths = [len(word) for word in ["hello", "world", "python"]]

a = [3,5,1,5,12,33,151]
b = [number*2 for number in a]
print(b)
