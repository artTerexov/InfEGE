def calc(n):
    if n == 25:
        return 1
    if n > 25:
        return 0
    return calc(n + 1) + calc(n * 3) + calc(n * 4)


print(calc(1))