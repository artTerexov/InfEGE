def f(x, y):
    if x == 35 and y <= 2:
        return 1
    if x > 35:
        return 0
    return f(x + 2, y) + f((x * 2, y) if x % 2 == 0 else (x * 2 + 1, y + 1))


print(f(2, 0))
