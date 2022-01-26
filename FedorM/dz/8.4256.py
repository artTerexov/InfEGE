import itertools

a = set(itertools.permutations("КУСАТЬ",r = 5))
c = 0
for i in a:
    b = ''.join(i)
    if b[0] != 'Ь' and "СУК" not in b:
        c += 1
print(c)