# Пифагоровой тройка назовём тройку чисел (a, b, c),
# такую что a ≤ b ≤ с и a2+b2=c2. Найдите все пифагоровы тройки,
# в которых все числа находятся в диапазоне [1; 5000].
# Запишите в ответе количество подходящих троек, а затем –
# значение c для тройки, в которой сумма a+b+c максимальна.

import time
start_time = time.time()

buff = []
maxSum = 0
maxC = 0
for a in range(1, 5001):
    for b in range(a + 1, 5001):
        c = int((a ** 2 + b ** 2) ** 0.5)
        if c ** 2 == (a ** 2 + b ** 2) and (a <= b <= c) and c <= 5000:
            buff.append(c)
            if maxSum < a + b + c:
                maxC = c
                maxSum = a + b + c
print(len(buff), maxC)

print("--- %s seconds ---" % (time.time() - start_time))