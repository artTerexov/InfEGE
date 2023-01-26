for N in range(1, 100):
    n = bin(N)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    R = int(n, 2)
    if R > 80:
        print(N, R)
