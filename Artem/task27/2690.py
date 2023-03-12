with open('files/2690_B.txt') as f:
    n = [[int(j) for j in i.split()] for i in f.readlines()]
n.pop(0)

D = 7

k = [0]

for i in n:
    coombinations = [x + y for x in i for y in k]
    k = {x % D: x for x in sorted(coombinations, reverse=True)}
    k = k.values()

print(min([x for x in k if x % D != 0]))

# 4913 15089332