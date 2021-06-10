for i in range(1, 1000):
    x = i
    L = 0
    M = 1
    while x > 0:
        L = L + 1
        M = M * (x % 8)
        x = x // 8
    if L == 3:
        if M == 120:
            print(i)

