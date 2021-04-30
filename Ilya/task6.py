for i in range(-1000, 81):
    s = i
    n = 1
    while s <= 80:
        s = s + 7
        n = n * 3
    if n == 81:
        print(i)