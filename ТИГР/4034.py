def f(a, b, c, m):
    if a + b >= 90:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 3, b, c + 1, m), f(a, b * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for b in range(1, 81):
    for m in range(1, 5):
        if f(9, b, 0, m) == 1:
            if m == 4:
                print(b, m)
                break