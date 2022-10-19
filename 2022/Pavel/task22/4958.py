for i in range(1, 1000):
    x = i
    a = 4
    b = 10
    while x > 0:
        a += 1
        if x % 2 == 1:
            b += x % 64
        x //= 8
    if a == 7 and b == 18:
        print(i)
