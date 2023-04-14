import math


def test(s):
    minCost = 10 ** 10
    n = 0
    for i in range(len(s)):
        cost = 0
        for j in range(len(s)):
            cost += math.ceil(s[j][1] / 100) * abs(s[j][0] - s[i][0])
        if minCost > cost:
            n = s[i][0]
            minCost = cost
    return n


with open("27A_6638.txt") as f:
    y = [[int(j) for j in i.split()] for i in f.readlines()]

print(test(y))
