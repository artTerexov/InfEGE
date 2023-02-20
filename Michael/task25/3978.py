for N in range(150000000, 300000001):
    for m in range(1, 28, 2):
        for n in range(0, 17, 2):
            if N == 2 ** m * 3 ** n:
                print(N, m + n)

