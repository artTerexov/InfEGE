# Ниже записана программа, которая вводит натуральное число x, выполняет
# преобразования, а затем выводит два числа. Укажите наименьшее возможное
# значение x, при вводе которого программа выведет числа 4 и 11.

for i in range(0, 10000):
    x = i
    k = x % 8
    a = 0
    b = 0
    while x > 0:
      d = x % 8
      if d == k:
        a += 1
      b += d
      x //= 8
    if a == 4 and b == 11:
        print(i)