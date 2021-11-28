for h in range(50, 200):
    x = h
    S = 0
    while x > 0:
        if x % 2 > 0:
            S = S + (x % 7)
        else:
            S = S - (x % 7)
        x = x // 7
    if S == 1:
        print(h)
        break
