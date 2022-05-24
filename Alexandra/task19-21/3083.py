def f(h1, c, m):
    if 60 >= h1 >= 36:
        return c % 2 == m % 2
    if h1 > 60 and c % 2 != m % 2:
        return 1
    if c == m or h1 > 60:
        return 0
    h = [f(h1 + 1, c + 1, m), f(h1 * 2, c + 1, m), f(h1 * 3, c + 1, m)]
    # В 19 задаче меняем вторую функцию all на any
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 19 задача m = 2
# 20 задача m = 3
# 21 задача m = 4
for i in range(1, 36):
    if f(i, 0, 4):
        print(i)
