# +-*//
def add(a,b):
    return a + b

def min(c,d):
    return c - d

def mul(e,f):
    return e*f

def na(e,f):
   return e//f

def guide():
    print("""사용 하실 프로그램을 고르세요.
        1. 
        2.
        3.
        4. 
        5. 
        """)
def getNumbers():
    a = int(input("첫 번째 숫자 입력"))
    b = int(input("두 번째 숫자 입력"))
    return  a,b
# def getNumbers2():
#     c = int(input("첫 번째 숫자 입력"))
#     d = int(input("두 번째 숫자 입력"))
#     return c,d
# def getNumbers3():
#     e = int(input("첫 번째 숫자 입력"))
#     f= int(input("두 번째 숫자 입력"))
#     return e,f
# def getNumbers4():
#     g = int(input("첫 번째 숫자 입력"))
#     h = int(input("두 번째 숫자 입력"))
#     return g//h

#while 1. 2 3 4 5번 종료하는 프로그램.
# variety = input("add(a,b) min(c, d) mul(e,f) na(e,f) 중 하나의 함수를 선택해주세요")
while True:
    guide()
    systemCode = int(input("숫자 입력:"))
    if (systemCode == 1):
        a,b = getNumbers()
        add(a,b)
    elif systemCode == 2:
        c, d = getNumbers()
        min(c, d)
    elif systemCode == 3:
        e, f = getNumbers()
        mul(e,f)
    elif systemCode == 4:
        a,b = getNumbers()
        na(a,b)
    else:
        break
print()



