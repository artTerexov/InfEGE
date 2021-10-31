for h in range(1, 100):
    s = h
    n = 32
    while n > s:
        s = s + 1
        n = n - 1
    if s == 30:
        print(h)
