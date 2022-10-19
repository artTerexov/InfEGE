# Рассматриваются целые числа, принадлежащих числовому отрезку [356712; 420901],
# которые представляют собой произведение трёх различных простых делителей, оканчивающихся на одну и ту же цифру.
# В ответе запишите количество таких чисел и их среднее арифметическое (только целую часть числа)

import time

start = time.time()


def isSimple(num):
    for k in range(2, int(num ** 0.5) + 1):
        if num % k == 0:
            return False
    return True


result = []
for i in range(356712, 420901 + 1):
    a = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if isSimple(j):
                a.add(j)
            if isSimple(i // j):
                a.add(i // j)
    if len(a) == 3:
        a = list(a)
        if str(a[0])[-1] == str(a[1])[-1] == str(a[2])[-1] and a[0] * a[1] * a[2] == i:
            result.append(i)

print(len(result), sum(result) // len(result))

print(time.time() - start)

