# Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде произведения двух
# натуральных чисел и найдём для каждого такого произведения разность сомножителей. Например, для числа 18 получим:
# 18 = 18*1 = 9*2 = 6*3, множество разностей содержит числа 17, 7 и 3. Подходящей будем называть пару сомножителей,
# разность между которыми не превышает 110. Найдите все натуральные числа, принадлежащие отрезку [1000000; 1500000],
# у которых есть не менее трёх подходящих пар сомножителей. В ответе перечислите найденные числа в порядке возрастания,
# справа от каждого запишите наибольший из всех сомножителей, образующих подходящие пары.

import time
start_time = time.time()

for i in range(1000000, 1500000 + 1):
    s = []
    deli = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if abs(i // j - j) <= 110:
                s.append(abs(i // j - j))
                deli.append(j)
                deli.append((i // j))
    if len(s) >= 3:
        print(i, deli[1])

print("--- %s seconds ---" % (time.time() - start_time))