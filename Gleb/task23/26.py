def calc(num, flag):
    if num == 29 and flag == 1:
        return 1
    if num > 29:
        return 0
    if num == 25:
        return 0
    if num == 14:
        flag += 1
    return calc(num + 1, flag) + calc(num * 2, flag)


print(calc(2, 0))