for i in range(0, 1000):
    s = i
    n = 1
    while s < 208:
        s = s + 20
        n = n * 2
    if n == 256:
        print(i)