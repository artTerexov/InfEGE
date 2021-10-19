for s in range(0, 100000):
    result = s
    n = 1
    while s > 200:
        s -= 15
        n += 3

    if n == 46:
        print(result)