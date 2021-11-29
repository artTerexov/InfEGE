# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
# Считайте четыре действительных числа и выведите результат работы этой функции.


def distance(a, b, c, d=6.0):
    print(d)
    dist = ((c - a) ** 2 + (d - b) ** 2) ** 0.5
    print(dist)


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

distance(x1, x2, y1, y2)

