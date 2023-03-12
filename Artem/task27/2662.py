with open('files/2662_A.txt') as f:
    n = [[int(j) for j in i.split()] for i in f.readlines()]
n.pop(0)

D = 3

k = [0]

for i in n:
    coombinations = {x + y for x in i for y in k}
    k = {x % D: x for x in sorted(coombinations)}
    k = k.values()

print(k.mapping.get(0))
