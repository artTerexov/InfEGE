def f(s, c, m, flag):
    if s >= 20:
        return c % 2 == m % 2
    if c == m:
        return 0
    if flag == 0:
        h = [f(s * 2, c + 1, m, flag), f(s + 2, c + 1, m, flag), f(s, c + 1, m, flag + 1)]
    else:
        h = [f(s * 2, c + 1, m, flag), f(s + 2, c + 1, m, flag)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 20):
    for m in range(1, 10):
        if f(s, 0, m, 0):
            print(s, m)
            break

# 1
# 2 3 1