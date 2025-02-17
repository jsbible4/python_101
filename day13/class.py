class Car:
    #self는 자기 클래스 안에 누구?
    # self 자기 참조 연산자
    def __init__(self,n,g):
        self.name = n
        self.gas = g
        self.stateModes = ['p', 'd', 'n', 'r']
        self.state = 'p'
    def driving(self):
        if self.state == 'd':
            print(f'{self.name}가(이) 주행중!')
            self.gas -= 10
        else:
            print(f'현재 상태는 {self.state}입니다. 기어를 수정하세요')
    def gearing(self, state):
        if state in self.stateModes:
            self.state = state
        else:
            print(f'해당 기어가 없습니다.')

a = Car('기아',300)
a.driving()
a.gearing('k')
a.gearing('d')
a.driving()

print(a.name,a.gas)

# circle class를 만들고 둘레랑 넓이를 뱉는 함수를 만들어주세욤!

class Circle:
    def __init__(self,r):
        self.radius = r
    def circumference(self):
        self.circumference = self.radius*2*3.14
        return self.circumference
    def area(self):
        self.area = self.radius**2*3.14
        return self.area


# class Circle:
#     def __init__(self, radius):
#         self.r = radius
#         self.pi = 3.14
#     def width(self):
#         return self.r * 2 * self.pi
#     def round(self):
#         return  self.r * 2 * self.pi

a = Circle(10)
print(f'반지름이 {self.radius}일 때, 원의 둘레는 {self.circumference}입니다. ')
print(f'반지름이 {self.radius}일 때, 원의 넓이는 {self.area}입니다.')
# b = Circle(30)
# print(b.width())
# print(b.round())



