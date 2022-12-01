for N in range(749, 0, -1):
    n = bin(N)[2:]
    for i in range(3):
        if n.count('0') == n.count('1'):
            n = n + n[-1]
        elif n.count('0') > n.count('1'):
            n = n + '1'
        else:
            n = n + '0'
    R = int(n, 2)
    if R % 2 == 0 and R % 4 != 0:
        print(N)
        break
