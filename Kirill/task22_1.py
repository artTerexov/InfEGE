# Ниже записана программа, которая вводит натуральное число x, выполняет
# реобразования, а затем выводит два числа. Укажите наименьшее возможное значение x,
# при вводе которого программа выведет числа 5 и 16.

for i in range(-10000, 10000):
    x = i
    m = 0
    s = 0
    while x > 0:
        d = x % 6
        s += d
        if d > m:
            m = d
        x = x // 6
    if m == 5 and s == 16:
        print(i)