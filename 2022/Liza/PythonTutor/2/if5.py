# Даны три целых числа. Выведите значение наименьшего из них.

x = int(input())
y = int(input())
z = int(input())

if (x > y) and (y < z):
    print(y)
elif (x < y) and (x < z):
    print(x)
elif (x == y) and (y < z):
    print(x)
else:
    print(z)