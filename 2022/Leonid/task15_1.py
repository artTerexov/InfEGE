# x & 25 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)

for A in range(0, 10000):
    for x in range(0, 10000):
        F = (x & 25 == 0) or (x & 17 != 0 or x & A != 0)
        if F == 0:
            break
    if F == 1:
        print(A)
        break
