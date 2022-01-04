# Напишите программу, которая находит 6 простых чисел наиболее приближенные к числу 10000000 (10 миллионов).
# Причем 3 найденных числа должны быть меньше 10000000, остальные 3 числа – больше.
# Найденные числа расположите в порядке возрастания. В качестве ответа выведите пары
# чисел – расстояние от найденного числа до 10000000 и само число.


buff = []
num = 10000000
while len(buff) != 3:
    num += 1
    dell = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            dell += 1
            break
    if dell == 0:
        buff.append([abs(10000000 - num), num])


print(buff)

# [[19, 10000019], [79, 10000079], [103, 10000103]]
# [[9, 9999991], [27, 9999973], [29, 9999971]]