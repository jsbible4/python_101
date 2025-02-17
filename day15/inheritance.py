# Inheritance

class SmartPhone:
    def __init__(self, os, cpu, ram, company):
         self.os = os
         self.cpu = cpu
         self.ram = ram
         self.company = company
    def calling(self):
        print('전화중')

class Galaxy(SmartPhone):
    def __init__(self, os, cpu, ram, company, finger):
        super().__init__(os, cpu, ram, company)
        self.finger = finger
    def samsungPay(self):
        print('돈이 세어 나가는 중')

class Iphone(SmartPhone):
    def __init__(self, os, cpu, ram, company, face):
        super().__init__(os, cpu, ram, company)
        self.face = face
    def connect(self, device):
        print(f'{device} 연동중')

s23 = Galaxy('안드로이드','a','8GB','삼성','새끼손가락')
s23.samsungPay()
s23.calling()

iphone15 = Iphone('IOS', 'b', '8GB', 'apple', 'myface')
iphone15.connect('mac')
iphone15.calling()


class Shape:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print(f' I am {self.name}.')
    def getArea(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def getArea(self):
        print(f'{self.radius**3.14}')

class Rectangle(Shape):
    def __init__(self, name, ver, hor):
        super().__init__(name)
        self.ver = ver
        self.hor = hor

    def getArea(self):
        print(f'{self.ver*self.hor}')

class Triangle(Shape):
    def __init__(self, name, height, base):
        super().__init__(name)
        self.height = height
        self.base = base

    def getArea(self):
        print(f'{self.height*self.base*0.5}')


