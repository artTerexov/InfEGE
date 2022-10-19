# (№ 3751) Найдите все натуральные числа, принадлежащие отрезку [100 000 000; 101 000 000], у
# которых ровно три различных чётных делителя. В ответе перечислите найденные числа в порядке
# возрастания, справа от каждого числа запишите его второй по величине нетривиальный делитель
# (не равный 1 и самому числу).

import time
start_time = time.time()

for i in range(100000000, 101000000 + 1):
    d = set()
    count = 0
    if i % 2 != 0:
        continue
    for n in range(1, int(i ** 0.5) + 1):
        if i % n == 0:
            if n % 2 == 0:
                count += 1
            if (i // n) % 2 == 0:
                count += 1
            d.add(n)
            d.add(i // n)
            if count > 3:
                break
    if count == 3:
        d = list(d)
        d.sort()
        print(i, d[2])

print("--- %s seconds ---" % (time.time() - start_time))