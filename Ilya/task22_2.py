for i in range(0, 1000):
    a = i
    R = 17
    L = 0
    while a >= R:
        L = L + 1
        a = a - R
    M = a
    if M < L:
        M = L
        L = a
    if L == 11 and M == 14:
        print(i)