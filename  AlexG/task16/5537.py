import sys

# F(n) = 1, если n = 1
# F(n) = n·F(n – 1), если n > 1.

sys.setrecursionlimit(3000)


def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


# 2023 * 2022 * 2021 * 2020...  * 1
#        2020 * 2019 * 2018 ... * 1
print(F(2023) / F(2020))
print(2023 * 2022 * 2021)
