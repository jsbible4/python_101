# number = input("숫자 입력")
# sum = 0
# for i in number:
#     sum += int(i)
# print(sum)
#
# n = 3
# two_list = []
# for i in [4, 5, 6, 7, 8, 9, 10]:
#     if i % n == 0:
#         two_list.append(i)
# print(two_list)

k = input("아무 숫자 한 자릿 수 입력.")
for i, j in enumerate("183"):
    if j == k:
        print( i + 1 )
        break
