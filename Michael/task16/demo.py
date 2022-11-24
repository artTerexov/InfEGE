import sys

sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())


def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print(F(2023) / F(2020))