for i in range(0, 1000):
    s = i
    n = 80
    while s + n < 160:
        s = s + 15
        n = n - 10
    if s <= 100:
        print(i)
        break
