# Рассматриваются целые числа, принадлежащих числовому отрезку [356712; 420901], которые представляют
# собой произведение
# трёх различных простых делителей, оканчивающихся на одну и ту же цифру.
# В ответе запишите количество таких чисел и их
# среднее арифметическое (только целую часть числа).

import time

start = time.time()

prime_div = []
for i in range(3, 100000):
    count = 0
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        prime_div.append(i)
prime_div.remove(5)

numbers = []
for i in range(356712 + 1, 420901 + 1, 2):
    count = 0
    b = []
    for j in prime_div:
        if i % j == 0:
            count += 1
            b.append(j)
            if count > 3:
                break
    if len(b) == 3 and b[0] * b[1] * b[2] == i:
        # print(b)
        if b[0] % 10 == b[1] % 10 == b[2] % 10:
            numbers.append(i)
print(len(numbers), int(sum(numbers) / len(numbers)))

print(time.time() - start)