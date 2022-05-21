for N in range(1, 1000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n += '10'
    else:
        n = '1' + n + '01'
    R = int(n, 2)
    if R > 516:
        print(N)
        break