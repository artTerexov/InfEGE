for s in range(1, 100):
    x = s
    a = 1
    b = a
    while a < x:
        c = a + b
        a = b
        b = c
    if b == 55:
        print(s)
