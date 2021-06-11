c = 0
for N in range(10, 1000):
    n = str(bin(N))[2:]
    n += n[-2]
    n += n[1]
    if 100 <= int(n, 2) <= 150:
        c += 1
        print(n)
print(c)
