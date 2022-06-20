minCHE = 10000000000
for n in range(1, 1000):
    i = bin(n)[2:]
    if n % 2 == 0:
        i = '10' + i + '10'
    else:
        i = '1' + i + '00'
    f = int(i, 2)
    if f > 100:
        if f < minCHE:
            minCHE = f
print(minCHE)
