for h in range(0, 500):
    x = h
    S = 0
    while x > 0:
        if x % 5 > 0:
            S = S + (x % 5)
        else:
            S = S * (x % 5)
        x = x // 5
    if S == 13:
        print(h)
