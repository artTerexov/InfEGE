# Рассматривается множество целых чисел, принадлежащих отрезку [1170; 8367],
# которые делятся на 3 или на 7 и не делятся на 11, 13, 17 и 19.
# Найдите количество таких чисел и минимальное из них. В ответе
# запишите два числа через пробел: сначала количество, затем минимальное число.

buff = []
for i in range(1170, 8368):
    if (i % 3 == 0 or i % 7 == 0) and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
        buff.append(i)
print(len(buff), min(buff))