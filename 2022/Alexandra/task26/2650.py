# Магазин предоставляет оптовому покупателю скидку по следующим правилам:
# − на каждый второй товар ценой больше 200 рублей предоставляется скидка 30%;
# − общая цена покупки со скидкой округляется вверх до целого числа рублей;
# − порядок товаров в списке определяет магазин и делает это так, чтобы общая сумма скидки была наименьшей.
# Вам необходимо определить общую цену закупки с учётом скидки и цену самого дорогого товара, на который будет
# предоставлена скидка.

import math

with open('files/2650.txt') as f:
    a = f.read().strip().split('\n')

a.pop(0)
budget = 0
exp = []
max_exp = []
sales = 0
for i in a:
    if int(i) > 200:
        exp.append(int(i))
    else:
        budget += int(i)
exp.sort()
for i in range(len(exp)):
    if i < len(exp) // 2:
        sales += exp[i]
        # budget += math.ceil(0.7 * exp[i])
        max_exp.append(exp[i])
    else:
        budget += exp[i]

print(budget + math.ceil(0.7 * sales), max(max_exp))
