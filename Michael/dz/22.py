k = 0
for i in range(-1000, 1000):
    s = i
    P = 20
    Q = 13
    K1 = 0
    K2 = 0
    while s < 230:
        s += P
        K1 += 1

    while s >= Q:
        s -= Q
        K2 += 1

    if K1 == 12 and K2 == 18:
        k += 1


print(k)