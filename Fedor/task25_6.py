# Среди целых чисел, принадлежащих числовому отрезку [173225; 217437],
# найдите числа, которые представляют собой произведение двух различных простых
# делителей, заканчивающихся на одну и ту же цифру. Запишите в ответе количество таких чисел и минимальное их них.

def is_simple(n):
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


buff = []
for i in range(173225, 217438):
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0 and is_simple(j) and is_simple(i // j):
            d1 = j
            d2 = i // j
            if d1 != d2 and d1 % 10 == d2 % 10:
                buff.append(i)
print(len(buff), min(buff))

