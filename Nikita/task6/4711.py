for i in range(1, 1000):
    s = i
    n = 1
    while n < 1024:
        s = s + 2 * n
        n = n + s
    if n == 1961:
        print(i)
