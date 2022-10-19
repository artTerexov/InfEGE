def calc(start, end, flag):
    if start == end and flag == 1:
        return 1
    if start < end:
        return 0
    if start == 43:
        flag += 1
    return calc(start - 8, end, flag) + calc(start // 2, end, flag)


print(calc(102, 5, 0))
