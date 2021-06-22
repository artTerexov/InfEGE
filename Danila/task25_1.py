# Напишите программу, которая ищет среди целых чисел, принадлежащих
# числовому отрезку [3532000; 3532160], простые числа.
# Выведите все найденные простые числа в порядке возрастания,
# слева от каждого числа выведите его номер по порядку.

import datetime

start = datetime.datetime.now()

for i in range(3532000, 3532161):
    b = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            b.append(j)
        if len(b) > 0:
            break
    if len(b) == 0:
        print(i)

end = datetime.datetime.now()

print(end - start)