import functools


@functools.lru_cache(maxsize=None)
def G(n):
    if n <= 0:
        return 2
    if n > 0 and n % 2 != 0:
        return F(n - 1) - 2 * G(n - 2)
    if n > 0 and n % 2 == 0:
        return 2 * F(n - 2) - 2 * G(n - 1)


@functools.lru_cache(maxsize=None)
def F(n):
    if n <= 2:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n - 1) - n
    if n > 2 and n % 2 == 0:
        return F(n - 2) + G(n - 1) + 2


print(F(96))