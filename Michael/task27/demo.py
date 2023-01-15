import math

with open('files/demo_B.txt') as f:
    s = [[int(j) for j in i.split()[::-1]] for i in f.readlines()]
# s.sort(reverse=True)
minCost = []
for j in range(len(s)):
    cost = 0
    for i in range(len(s)):
        if i != j:
            cost += abs(s[j][1] - s[i][1]) * math.ceil(s[i][0] / 36)
    minCost.append(cost)

print(min(minCost))


# 51063 5634689219329
