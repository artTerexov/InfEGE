for i in range(100, 1000):
    x = i
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 5
        x = x // 5
    if a == 2 and b == 6:
        print(i)



