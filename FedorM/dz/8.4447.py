import itertools
a = set(itertools.permutations('марина', r=6))
c = 0
for i in a:
    d = ''.join(i)
    if d[0] not in 'аяюэоиуеёы':
        c += 1
print(c)