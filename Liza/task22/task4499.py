for i in range(1, 1000):
    k = i
    x = 1
    y = x
    while k < 13:
        k += 1
        if k == 7:
            t = 0
        else:
            t = x + y
        x = y
        y = t
    if k == 13 and x == 25:
        print(i)
