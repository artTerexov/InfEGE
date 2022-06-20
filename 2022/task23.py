def calc(num, flag):
    if num == 1 and flag == 1:
        return 1
    if num < 1:
        return 0
    if num == 12:
        flag += 1
    return calc(num - 1, flag) + calc(num // 2, flag)


print(calc(30, 0))
