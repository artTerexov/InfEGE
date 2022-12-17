def calc(n, flag):
    if n == 29 and flag == 1:
        return 1
    if n > 29 or n == 25:
        return 0
    if n == 14:
        flag += 1
    return calc(n + 1, flag) + calc(n * 2, flag)


print(calc(2, 0))