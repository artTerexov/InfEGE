for i in range(1, 100000):
    N = str(i)
    S1 = 0
    S2 = 0
    for j in range(len(N)):
        if (j + 1) % 2 != 0:
            S2 += int(N[j])
        if int(N[j]) % 2 == 0:
            S1 += int(N[j])
    R = abs(S1 - S2)
    if R == 27:
        print(i)