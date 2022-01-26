import itertools

a = set(itertools.product("01234567", repeat=4))
c = 0

for i in a:
    d = ''.join(i)
    if int(d[0]) % 2 == 0 and (int(d[0]) >= int(d[1]) >= int(d[2]) >= int(d[3])) and d[0] != '0':
        c += 1
print(c)
