c = 0
for n in range(2, 10000):

    r = bin(n)[2:]
    r = r + str(r[-2])
    r = r + str(r[1])
    if 150 < int(r, 2) < 201:
        c += 1
print(c)