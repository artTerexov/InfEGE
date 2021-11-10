# (№ 4123) (С. Неретин) Пифагоровой тройка назовём тройку чисел (a, b, c), такую что a ≤ b ≤ с и a**2+b**2=c**2. Найдите все
# пифагоровы тройки, в которых все числа находятся в диапазоне [1; 5000]. Запишите в ответе количество подходящих троек,
# а затем – значение c для тройки, в которой сумма a+b+c максимальна.
import math
import time

start_time = time.time()

k = 0
cMax = 0
m = 0
for i in range(1, 5001):
    for j in range(i, 5001):
        c = int(math.sqrt(i ** 2 + j ** 2))
        if i ** 2 + j ** 2 <= 5000 ** 2 and c ** 2 == (i ** 2 + j ** 2) and i <= j:
            k += 1
            if j + i + c > m:
                cMax = c
                m = j + i + c
print(k, cMax)

print("--- %s seconds ---" % (time.time() - start_time))
