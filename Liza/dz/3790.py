for h in range(1, 10000):
    x = h
    k = x % 8
    a = 0
    b = 0
    while x > 0:
        d = x % 8
        if d == k:
            a += 1
        b += d
        x //= 8
    if a == 3 and b == 20:
        print(h)
        break
