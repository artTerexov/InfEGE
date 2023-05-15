for n in range(1, 10000000):
    N = str(n)
    s1 = 0
    for i in N:
        if int(i) % 2 != 0:
            s1 += int(i)
    s2 = 0
    for j in range(len(N)):
        if j % 2 != 0:
            s2 += int(N[j])
    R = abs(s1 - s2)
    if R == 29:
        print(n)