# Ниже записан алгоритм. Получив на вход число x,
# этот алгоритм печатает два числа a и b. Укажите наибольшее из таких чисел x,
# при вводе которых алгоритм печатает сначала 2, а потом 5.

for i in range(1, 100000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 100)
        x = x // 100
    if a == 2 and b == 5:
        print(i)
