from itertools import product

x = sorted(product("СТЕКЛО", repeat=5))
c = 0
z = 0

for i in x:
    n = ''.join(i)
    z += 1
    if n[0] == "С" and n.count("ОО") == 1:
        c += 1
        print(z, n)
print(c)

print(int('40033', 6))