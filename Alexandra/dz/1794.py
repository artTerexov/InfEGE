for i in range(1, 10000):
    s = i
    n = 100
    while s - n >= 100:
        s = s + 20
        n = n + 40
    if i != s:
        print(i)
        break