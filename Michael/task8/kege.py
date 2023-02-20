from itertools import product

a = set(product("0123456", repeat=6))
c = 0
for i in a:
    el = ''.join(i)
    if el[0] != "0" and el.count('6') == 1 and all(int(el[n]) % 2 != int(el[n + 1]) % 2 for n in range(len(el) - 1)):
        # flag = True
        # for n in range(len(el) - 1):
        #     if int(el[n]) % 2 == int(el[n + 1]) % 2:
        #         flag = False
        #         break
        # if flag:
        c += 1
print(c)