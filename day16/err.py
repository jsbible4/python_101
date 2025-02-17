# 런타임에서 에러처리
# try~except

# try:
#     num = int(input('점수 입력'))
#     result = 10 / num
#     print(result)
# except ZeroDivisionError:
#     print('0으로 나눌 수 없음')
#
# try:
#     num = int(input('정수 입력'))
#     print(num + 5)
# except ValueError:  # 값이 틀릴 경우
#     print('숫자를 넣으세요')
# else:
#     print('잘했음')  # 정상적으로 코드가 끝나면 '잘했음'이 출력됨.

try:
    num = int(input('점수 입력'))
    result = 10 / num
    print(result)
# except ValueError:  # 값이 틀릴 경우
#     print('숫자를 넣으세요')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없음')
# else:
#     print('잘했음')

except Exception as e:   # Exception 안에 ValueError, ZeroDivisionError 가 포함되어있는거임. # as 는 ~~로 취급해주세요.
    print(f'다음 에러는 {e}임')
else:
    print('잘했음')
finally:
    print('무조건 나옴 끝')   # 에러가 나든 안 나든 무조건 나옴.
