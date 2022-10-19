for i in range(1, 1000):
    d = i
    n = 1
    s = 46
    while s <= 2700:
        s = s + d
        n = n + 4
    if n == 121:
        print(i)