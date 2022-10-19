for x in range(1, 100001):
    s10 = 0
    s3 = 0
    n3 = ''
    n10 = 27 ** 7 - 3 ** 11 + 36 - x
    y = n10
    while y > 0:
        n3 = str(y % 3) + n3
        y //= 3
    for i in range(len(n3)):
        s3 += int(n3[i])
    if s3 == 22:
        print(x)


