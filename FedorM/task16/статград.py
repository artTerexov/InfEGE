import functools
import math


@functools.lru_cache(maxsize=None)
def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return F(n // 2)
