def calc(n, f):
    if n == 38 and f == 1:
        return 1
    if n > 38:
        return 0
    if n == 6 or n == 16 or n == 26 or n == 36:
        return 0
    return calc(n + 1, f) + calc(n + 2, f) + calc(n * 2, f)


print(calc(1, 1))
