for x in range(10001):
    m = 0
    s = 0
    while x > 0:
        d = x % 7
        s += d
        if d > m:
            m = d
            x //= 7
    if m == 5 and s == 12:
        print(x)
