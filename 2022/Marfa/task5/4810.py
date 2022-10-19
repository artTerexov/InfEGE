for x in range(1, 4000000):
    s1 = 0
    s2 = 0
    x1 = str(x)
    for i in range(len(x1)):
        if int(x1[i]) % 2 != 0:
            s1 += int(x1[i])
        if i % 2 != 0:
            s2 += int(x1[i])
    s = abs(s1 - s2)
    if s == 30:
        print(x)
        break