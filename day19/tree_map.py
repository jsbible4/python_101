#squarify  n개의 여러개 사각형을 만들 수 있음.
import matplotlib.pyplot as plt
import squarify

coffee = ['Americano', 'latte', 'clod brew', 'dolce', 'mint', 'caramel', 'vanilla', 'milk tea']
sales = [120,90,60,110,20,70,90,110]
colors = ['black', 'white', 'darkgrey', 'skyblue', 'green', 'yellow', 'gold', 'brown']

squarify.plot(sizes=sales, label=coffee, color=colors, alpha = 0.8)  # alpha = 색의 찐하고 연한 정도
plt.show()
