print('메가커피 포스 프로그램!')
# 커피: 이름, 가격, 샷 개수
# 1. 커피 판매 - [커피리스트], 메뉴 고르라고 함 (몇 번), 개수, 끝
# 2. 커피 신메뉴 등록 - 이름, 가격, 샷 개수 --끝
# 3. 일일 매출확인 - 첫번째: 커피리스트, 총개수, 총금액   - 두 번째: 커피리스트, 총 개수, 총 금액
# 4. 종료

class Coffee:
    def __init__(self, name, price, shot):
        self.name = name
        self.price = price
        self.shot = shot
    def intro(self):
        return f'이름: {self.name}, 가격: {self.price}'
class Sale:
    def __init__(self, coffeeName, coffeePrice, time):
        self.coffeeName = coffeeName
        self.coffeePrice = coffeePrice
        self.time = time
    def intro(self):
        return f'이름: {self.coffeeName} \n 가격: {self.coffeePrice} \n 시간: {self.time}'

class MegaCoffeeProgram:
    def __init__(self):
        self.coffeeList = [Coffee('Americano',2500,2), Coffee('Latte', 3500, 2)]  # 여기가 바로 Coffee class를 만든 이유다.
        self.sales = []
    def execute(self):
        while(True):
            self.firstDepthExecute()
            systemNumber = int(input('번호 입력'))
            if systemNumber == 1:
               self.menu()  #선택 전 먼저 커피리스트를 보여준다.
               order = int(input('메뉴를 골라주세요 : '))
               time = input('판매된 시간: ')
               selectCoffee = self.coffeeList[order]
               self.sales.append(Sale(selectCoffee.name, selectCoffee.price,time))
            elif systemNumber == 2:
                name = input('커피 이름 : ')
                price = int(input('커피 가격 : '))
                shot = int(input('샷 개수 : '))
                self.coffeeList.append(Coffee(name,price,shot))
            elif systemNumber == 3:
                self.showSale()
            elif systemNumber == 4:
                print('프로그램 종료')
                break
            else:
                print('번호 입력 오류!')
    def firstDepthExecute(self):
        print("""
            1. 커피 판매하기
            2. 커피 등록하기
            3. 일일 매출 확인하기
            4. 종료
            """)
    def menu(self):
        for index,item in enumerate(self.coffeeList):
            print(f'{index}. {item.intro()}')
    def showSale(self):
        for index,item in enumerate(self.sales):
            print(f'{index}. {item.intro()}')
main = MegaCoffeeProgram()
main.execute()

