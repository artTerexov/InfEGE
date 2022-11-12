from itertools import product

c = 0

for j in 4, 5, 6:
    for i in set(product("оникс", repeat=j)):
        el = "".join(i)
        if el.count("с") == 3 and el.count("о") == 1:
            c += 1
            print(el)
print(c)
