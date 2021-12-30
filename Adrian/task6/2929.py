for i in range(1, 100000):
    x = i
    a = 0
    b = 0
    while x > 0:
        x = x // 9
        if x % 2 > 0:
            a = a + x % 9
        else:
            b = b + 1
    if a == 11 and b == 3:
        print(i)