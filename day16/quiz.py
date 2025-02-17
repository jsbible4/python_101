# 1. "01012341234" => "*******1234"
#"0212345678" => "******5678"
phoneNumber = "021234567"
new_phone = ''

for i,e in enumerate(phoneNumber):
    if len(phoneNumber)- i > 4:
        new_phone+= '*'
    else:
        new_phone += e
print(new_phone)



# 2. 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]dmf flxjsgkqslek.
n = 5846625298
n_str = str(n)
print(n_str)
n_list = list(n_str)  #하나의 문자열을 리스트에 담으면 음절단위로 찢어진다. split()쓰면 어절단위
print(n_list)
n_list.reverse()
print(n_list)
