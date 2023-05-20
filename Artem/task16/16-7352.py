import sys
import functools

sys.setrecursionlimit(9999)


@functools.lru_cache(True)
def f(n):
    if n < 2:
        return 7
    if n > 1:
        return 7 * f(n - 2)


print(7 ** (12950 // 2 + 1) / 7 ** 6473)

