def Kvadrat(k: list) -> bool:
    c = 0
    k.sort()
    print()
    summ = (max(k) + min(k)) ** 2
    norep = (sum(k) - (max(k) + min(k))) ** 2
    if summ > norep:
        return True
    else:
        return False


def Para(k: list) -> bool:
    for x in k:
        if k.count(x) > 1:
            return True
    return False


with open("files/5761") as n:
    a = [[int(j) for j in i.split()] for i in n.readlines()]

c = 0
for line in a:
    if Kvadrat(line) and Para(line):
        c += 1
print(c)
Para(a)
Kvadrat(a)

