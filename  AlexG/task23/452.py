def calc(n, f):
    if n == 21 and f == 1:
        return 1
    if n > 21:
        return 0
    if n == 18:
        return 0
    if n == 12:
        f += 1
    return calc(n + 1, f) + calc(n + 3, f)


print(calc(3, 0))