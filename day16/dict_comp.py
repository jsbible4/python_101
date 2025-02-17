# dict_comprehension
coffee = ['Latte', 'flat white', 'ainshupener','americano']
price = [3500, 4500, 5000, 2000, 500]
# shot = [2,3,3,2,1]
#
# zip()
print(list(zip(coffee,price)))
#print([{'coffe' : c, 'price' : p } for c,p in zip(coffee,price)])
menu = {i : {'coffe' : c, 'price' : p} for i,(c,p) in enumerate(zip(coffee,price))}
print(menu)
print(menu[3])
