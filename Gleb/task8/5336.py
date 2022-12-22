from itertools import product


a = set(product("012345678", repeat=5))
count = 0
for i in a:
    el = ''.join(i)
    if el[0] not in '1357' and el[-1] not in '18' and el.count('3') <= 1 and el[0] != '0':
        count += 1
print(count)
