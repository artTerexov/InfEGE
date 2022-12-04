for N in range(6, 7):
    # Строим двоичную запись числа N
    n = bin(N)[2:]
    # 2a
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    # 2б
    else:
        n = '11' + n[2:] + '1'
        # print(n)
    R = int(n, 2)
    if R > 40:
        print(N)
