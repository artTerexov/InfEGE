from itertools import product


def vowelCount(a):
    z = 0
    for k in a:
        if k in "АОУЫЭЕЁИЮЯ":
            z += 1
    return z


n = product('АНТИУОПЯ*', repeat=7)
c = 0

for i in n:
    el = ''.join(i)
    if el.count("*") == 1:
        p = el.split("*")
        l1 = p[0]
        l2 = p[-1]
        if (vowelCount(l2) - vowelCount(l1) == 1) or (vowelCount(l2) - vowelCount(l1) == -1):
            c += 1
print(c)