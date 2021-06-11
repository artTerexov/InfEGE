for i in range(1,1000):
    x = i
    L = 0; M = 0
    while x > 5:
        L = L + 1
        if M < (x % 10):
            M = x % 10
        x = x // 10

    if L == 3 and M == 7:
        print(i)