import sys

sys.setrecursionlimit(5500)


def f(n):
    if n == 1:
        return 1
    if n == 2100 and d:
        return a
    if n > 1:
        return n * f(n - 1) + 1


d = False
a = f(2100)
d = True
print(int(f(3303) / f(3300)))
