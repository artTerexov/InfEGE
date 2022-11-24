def rep(a: list) -> bool:
    c = 0
    for i in a:
        if a.count(i) > 1:
            c += 1
    return c > 1


def suma(a: list) -> bool:
    repit = []
    norep = []
    for i in a:
        if a.count(i) > 1:
            repit.append(i)
        else:
            norep.append(i)
    return sum(norep) % 2 != 0


with open('files/5650') as f:
    s = [[int(j) for j in i.split()] for i in f.readlines()]

c = 0
for i in s:
    if rep(i) and suma(i):
        c += 1
print(c)


