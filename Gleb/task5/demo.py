for N in range(1, 50):
    # Двоичная запись числа N
    n = bin(N)[2:]
    # 2a
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    # 2b
    else:
        n = '11' + n[2:] + '1'
    R = int(n, 2)
    if R > 40:
        print(N, R)
