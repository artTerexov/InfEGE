def F(num, flag):
    if num == 50 and flag == 1:
        return 1
    if num > 50:
        return 0
    if num == 24:
        flag += 1
    return F(num + 2, flag) + F(num * 2, flag)


print(F(1, 0))