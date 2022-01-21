for i in range(1,1000):
    c = 0
    x = i
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        c += 1
        if c == 10000:
            break

    if x % 2 == 0:
        L = L + x % 8
        x = x // 8
    if L == 12 and M == 3:
        print(i)

