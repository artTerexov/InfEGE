# Для интервала [33333;55555] найдите числа, которые кратны сумме своих простых делителей.
# В качестве ответа приведите числа, для которых сумма простых делителей больше 250,
# – сначала найденное число, затем сумму его простых делителей.
# Примечание: само число в качестве делителя не учитывается.
import functools
functools.lru_cache(maxsize=None)


# def isSimple(num):
#     for k in range(2, int(num ** 0.5) + 1):
#         if num % k == 0:
#             return False
#     return True


for i in range(33333, 55555 + 1):
    buff1 = []
    for l in range(2, int(i ** 0.5) + 1):
        buff = []
        for s in range(2, int(l ** 0.5) + 1):
            if l % s == 0:
                buff.append(s)
        if len(buff) == 0 and i % l == 0:
            buff1.append(l)
    if sum(buff1) > 250 and i % sum(buff1) == 0:
        print(i, sum(buff1))