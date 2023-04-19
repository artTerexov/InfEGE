import math


def test(s):
    minCost = 10 ** 10
    n = 0
    dist = len(s) // 2
    for i in range(len(s) // 2):
        cost = 0
        print("Текущие индексы", i, i - dist)
        for j in range(1, dist // 2 + 1):
            cost += s[i - j] * j + s[(i + j) % len(s)] * j
            cost += s[(i - dist) - j] * j + s[((i - dist) + j) % len(s)] * j
        print(cost)
        if minCost > cost:
            minCost = cost
    return minCost


with open("27-130a.txt") as f:
    y = [int(i) for i in f.readlines()]


print(test(y))