for i in range(10000, 1000000):
    for j in range(1, 100000):
        x = i
        y = j
        a = 0
        b = 0
        while x * y > 0:
            if x > 0:
                a = a + 1
            if y > 0 and y % 7 > b:
                b = y % 7
            x = x // 10
            y = y // 7
        if a == 4 and b == 5:
            print(i * j)
            break
    if a == 4 and b == 5:
        break
