for i in range(1, 100000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 1000)
        x = x // 1000
    if a == 2 and b == 11:
        print(i)