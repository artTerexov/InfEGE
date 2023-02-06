import sys


sys.setrecursionlimit(4000)


def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1) + 1


print(F(3303) / F(3300))
