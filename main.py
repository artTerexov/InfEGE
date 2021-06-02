for i in range(1, 1000):
    s = i
    n = 1
    while s < 50:
        s += s
        n = n * 8
    if n == 512:
        print(i)