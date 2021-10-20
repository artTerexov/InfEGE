for i in range(1, 1000):
    d = i
    n = 2
    s = 0
    while s <= 365:
        s = s + d
        n = n + 5
    if n == 67:
        print(i)
