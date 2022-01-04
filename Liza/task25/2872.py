# (№ 2872) (Д.Ф. Муфаззалов) Число называется недостаточным, если оно больше суммы своих собственных
# делителей (то есть всех положительных делителей, отличных от самого́ числа). Найдите
# количество недостаточных чисел из диапазона [2; 30000].


# import time
#
# start_time = time.time()

count = 0
for i in range(2, 30000 + 1):
    summa = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            summa += j
            if j != i // j:
                summa += i // j
    if i > summa:
        count += 1

print(count)

# print(time.time() - start_time)
