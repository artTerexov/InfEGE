
for N in range(100, 0, -1):
    N1 = str(bin(N)[2:])
    N2 = N1[::-1]
    N3 = int(N2, 2)
    if N3 == 13:
        print(N)
        break

