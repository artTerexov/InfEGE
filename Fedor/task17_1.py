# Рассматривается множество целых чисел, принадлежащих числовому отрезку [2476; 7857],
# которые удовлетворяют следующим условиям:
# − кратны 2, но не кратны 8;
# − цифра в разряде сотен не превосходит 7.
# Найдите количество таких чисел и среднее арифметическое минимального и максимального из них
# (для второго числа запишите только целую часть).

buff = []

for i in range(2476, 7858):
    if i % 2 == 0 and i % 8 != 0 and int(str(i)[1]) <= 7:
        buff.append(i)

print(len(buff), (min(buff) + max(buff)) // 2)
