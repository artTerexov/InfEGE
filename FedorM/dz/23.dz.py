def f(x, y):
    if x == 33 and y == 1:
        return 1
    if x > 33 or x == 30:
        return 0
    if x == 16:
        y += 1
    return f(x + 1, y) + f(x * 2, y)


print(f(2, 0))