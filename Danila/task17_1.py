# Рассматривается множество целых чисел, принадлежащих числовому отрезку [1016; 7937], которые
# делятся на 3 и не делятся на 7, 17, 19, 27. Найдите количество таких чисел и максимальное из них.
# В ответе запишите два целых числа: сначала количество, затем максимальное число.

b = []
for i in range(1016, 7938):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        b.append(i)


print(len(b), max(b))