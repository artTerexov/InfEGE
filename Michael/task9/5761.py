def Kvadrat(k: list) -> bool:
    norep = 0
    summ = (max(k) + min(k)) ** 2
    for i in k:
        norep += i ** 2
    norep = norep - ((max(k) ** 2) + (min(k) ** 2))
    return summ > norep


def Para(z) -> bool:
    for x in z:
        if z.count(x) > 1:
            return True
    return False


with open("files/5761") as n:
    a = [[int(j) for j in i.split()] for i in n.readlines()]

c = 0
for i in a:
    if Kvadrat(i) and Para(i):
        c += 1
print(c)

