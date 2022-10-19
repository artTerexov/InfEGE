import functools


@functools.lru_cache()
def F(n):
    if n <= 5:
        return n
    if n > 5 and n % 8 == 0:
        return n + F(n / 2 - 3)
    else:
        return n + F(n + 4)


for i in range(1, 1000):
    try:
        print(i, F(i))
    except RecursionError:
        continue
        # print('Error=', i)