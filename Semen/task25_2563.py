# Напишите программу, которая ищет среди целых чисел, принадлежащих
# числовому отрезку [3532000; 3532160], простые числа. Выведите все
# найденные простые числа в порядке возрастания, слева от каждого числа
# выведите его номер по порядку.

import time
start_time = time.time()

count = 0
for i in range(3532000, 3532160 + 1):
    buff = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            buff.append(j)
            if i // j not in buff:
                buff.append(i // j)
    if len(buff) == 2:
        count += 1
        print(count, i)

print("--- %s seconds ---" % (time.time() - start_time))
