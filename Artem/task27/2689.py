with open('files/2689_B.txt') as f:
    n = [[int(j) for j in i.split()] for i in f.readlines()]
n.pop(0)

D = 5

k = [0]

for i in n:
    c = [i[0] + i[1], i[0] + i[2], i[2] + i[1]]
    coombinations = [x + y for x in c for y in k]
    k = {x % D: x for x in sorted(coombinations)}
    k = k.values()

print(max([x for x in k if x % D != 0]))


# 25034
# 76468978