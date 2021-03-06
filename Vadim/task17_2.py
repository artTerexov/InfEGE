# Рассматривается множество целых чисел, принадлежащих числовому отрезку [1529; 9482],
# которые удовлетворяют следующим условиям:
# − запись в двоичной системе закачивается на 01;
# − запись в пятеричной системе заканчивается на 3.
# Найдите минимальное из таких чисел и их сумму. Гарантируется, что искомая сумма не превосходит 10**7.

b = []
for i in range(1529, 9483):
    if i % 5 == 3 and i % 2 == 1 and (i // 2) % 2 == 0:
        b.append(i)
print(min(b), sum(b))