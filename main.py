def calc(num, t):
    if num == 42:
        return 1
    if num > 42:
        return 0
    d = []
    for i in num + 1, num + 3, num * 2, num * 3:
        if i not in d:
            d.append(i)
        else:
            d.append(0)
    return calc(d[0] if d[0] != 0 else 43, t + '1') + calc(d[1] if d[1] != 0 else 43, t + '2') \
           + calc(d[2] if d[2] != 0 else 43, t + '3') + calc(d[3] if d[3] != 0 else 43, t + '4')


print(calc(2, ''))