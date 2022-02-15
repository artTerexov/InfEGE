# 2895
# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [2484292; 2484370], простые числа. Выведите все найденные простые числа в порядке возрастания,
# слева от каждого числа выведите его номер по порядку.

count = 0
for a in range(2484292, 2484370 + 1):
    d = set()
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            d.add(i)
            d.add(a // i)
    if len(d) == 2:
        count += 1
        print(count, a)

