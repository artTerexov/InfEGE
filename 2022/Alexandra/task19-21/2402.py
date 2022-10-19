def f(h1, h2, c, m):
    if h1 + h2 >= 68:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(h1 + 2, h2, c + 1, m), f(h1 * 2, h2, c + 1, m), f(h1, h2 + 2, c + 1, m), f(h1, h2 * 2, c + 1, m)]
    # В 19 задаче меняем вторую функцию all на any
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 19 задача m = 2
# 20 задача m = 3
# 21 задача m = 4
for i in range(1, 60):
    if f(7, i, 0, 4):
        print(i)
