for A in range(1, 10000):
    for x in range(1, 1000):
        F = not(x % A == 0) or (not(x % A == 0) or (x % 34 == 0) and (x % 51 == 0))
        if F == 0:
            break
    if F == 1:
        print(A)
        break
