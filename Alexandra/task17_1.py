# (П. Волгин) В файле 17-7.txt содержится последовательность целых чисел. Элементы
# последовательности могут принимать значения от 0 до 200 включительно. Рассматривается
# множество элементов последовательности, для которых сумма цифр кратна 3.
# Найдите количество таких чисел и максимальное из них.

s = list()
with open("17_files/17-7.txt") as f:
    for i in f:
        s.append(int(i))

buff = list()
for i in s:
    summ = 0
    for j in str(i):
        summ += int(j)
    if summ % 3 == 0:
        buff.append(i)
print(len(buff), max(buff))
