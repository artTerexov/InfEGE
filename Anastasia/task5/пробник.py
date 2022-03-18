for N in range(1, 100):
    n = bin(N)[2:]
    if N % 2 == 0:
        k = n.count('1')
        n += bin(k)[2:]
    else:
        n = '1' + n + '00'
    R = int(n, 2)
    if R > 215:
        print(N)
