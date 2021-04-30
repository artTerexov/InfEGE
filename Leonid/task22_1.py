for i in range(9, 1000):
    x = i
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    if L == 4 and M == 5:
        print(i)
