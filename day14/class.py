class Car:
    def __init__(self,color,brand,year):   # 초기화 시켜줌 # 매서드의 시크니처
        self.color = color
        self.brand = brand
        self.year = year     # 매서드의 매개변수들

    def introduce(self):
        print(f'이 자동차의 색깔은 {self.color} 브랜드는 {self.brand} 연식은 {self.year}입니다.')

a = Car("black", "hyundai", 2020)
b = Car("blue", "kia", 2022)
a.introduce()
b.introduce()

# class 연습하기
# 1. 은행 계좌 클래스(BankAccount)
# 속성: 계좌 번호, 소유자 이름, 잔액
# 메서드: 입금하기, 출금하기, 잔액 확인하기

class BankAccount:
    def __init__(self,UUID,owner,balance):
        self.UUID = UUID
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self,money):
        if self.balance < money:
            print(f'{self.owner}님의 잔액이 부족합니다.')
        else:
            self.balance -= money
    def check_of_balance(self):
        print(f'{self.owner}님의 현재 금액은 {self.balance}입니다.')

kim = BankAccount(1, 'kimJenny',0)
lee = BankAccount(2,'leeNahyeong',0)

kim.deposit(5000)
kim.check_of_balance()
lee.withdraw(5000)

