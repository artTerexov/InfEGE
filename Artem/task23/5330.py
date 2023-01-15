def calc(num, f):
    if num == 1 and f == 1:
        return 1
    if num < 1:
        return 0
    if num == 10:
        f += 1
    return calc(num - 2, f) + calc(num // 2, f)


print(calc(28, 0))