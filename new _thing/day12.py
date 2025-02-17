# 1. 문자열 뒤집기
def string(my_string):
    re = my_string[::-1]
    return re
print(string("hello"))


# 2. 미완성된 할 일 찾기
# todo_list 에 있는 할 일 중, finished 배열을 통해 아직 끝내지 못한 일들을 찾아 순서대로 배열에 담아 반환한다.

def todo(todo_list, finished):
    done_list = [todo_list[i] for i in range(len(todo_list)) if not finished[i]]
    return done_list


todolist = todo(["priblem_solving", "practiceguitar", "swim", "studygraph"], [True,False,True,False])
print(todolist)





# 3. 암호 해독하기
# cipher 라는 문자열에서 code의 배수 번째 글자만 추출해 진짜 암호를 해독함.
cipher = 'hewvsejrnymosnwev'
real_cipher = ''
for i,f in enumerate(cipher):
    if i % 2 == 1:
        real_cipher += f
print(real_cipher)

