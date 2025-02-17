#람다함수: 간결하고 익명의 한 줄 함수로, 작은 연산이나
def add(x,y):
    return x + y
a = lambda x, y: x + y    #(왼쪽은 매개변수 :오른쪽은 결과값을 담는다)
print(a(10,20))
minus = lambda x,y: x - y
multi = lambda x,y: x * y

print(minus(20,5))
print(multi(40,50))

todo = lambda todo_list, finished: [todo_list[i] for i in range(len(todo_list)) if not finished[i]]
print(todo(["priblem_solving", "practiceguitar", "swim", "studygraph"], [True,False,True,False]))



# 콜백 함수
def ready(food):
    print(f"준비중: {food}")
def done(food):
    print(f"요리완료: {food}")

def cooking(food, making):
    menu = {
        1: 'chicken',
        2: 'meat',
        3: 'lamp'
    }
    making(menu[food])

cooking(2,ready)
cooking(3,done)


# 🥚 = > 🍜🍩🥙🥐
egg1 = '🥚'
egg2 = '🥚'
egg3 = '🥚'

def make_donut(egg):
    return '🍩'
def make_sandwich(egg):
    return  '🥙'
def make_crossant(egg):
    return '🥐'
def make_ramen(egg):
    return '🍜'
def cooking_egg(egg, cooking):
    cooking(egg)

cooking_egg(egg1, make_donut)


#내장함수 3대장
#map (콜백함수, [리스트, 문자열...])
number_list = [1,2,3,4,5]
new_list = list(map(lambda x:x+1,number_list))
print(new_list)
multi_list = list(map(lambda x:x**2,number_list))
print(multi_list)

words = ['happly','sad','mega','coffee','flower']
words_spelling_count = list(map(len,words))   #callback 함수가 len 자리니까 함수 len을 넣으면 됨. 굳이 만들어 쓸 필요 없음!
print(words_spelling_count)                   #len() == 0 이기 때문에 ()를 넣으면 안된다.


#철자 a가 들어있으면 살아남는 리스트
words = ['apple','banana', 'cherry', 'kiwi']
only_a = filter(lambda x: 'a' in x , words)
print(list(only_a))


from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x * y, numbers,4)
print(product)
