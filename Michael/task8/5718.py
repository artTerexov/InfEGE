from itertools import product

c = 0

for i in product("АНТИУОПЯX", repeat=7):
    el = "".join(i)
    if el[0] != 'А' and el[-1] != 'Я' and el[0] != 'X' and el[-1] != 'X' and el.count('X') == 1:
        c += 1
print(c)

print(7 ** 2 * 8 ** 4 * 5)