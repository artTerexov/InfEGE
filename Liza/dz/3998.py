
for s in range(1, 100):
    x = s
    a = 3 * x - 112
    b = 3 * x + 58
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 34:
        print(s)

