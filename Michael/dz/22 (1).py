for i in range(1, 1000000):
    s = i
    P = 29
    Q = 11
    K1 = 0
    K2 = 0
    while s != 2520:
        s = s + P
        K1 = K1 + 1
        if K1 > 314:
            break
    while s != Q + K1 + K2:
        s = s - Q
        K2 = K2 + 1
        if K2 > 470:
            break
    K1 += s
    K2 += s
    if K1 == 314 and K2 == 470:
        print(i)
        break

# 2520 - 11
# 11 + K1 + K2
