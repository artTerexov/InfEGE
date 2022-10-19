for A in range(1, 1000):
    for x in range(1, 1000):
        F = ((x % A != 0) or (x % 24 != 0) or (x % 16 == 0)) or (x % A != 0)
        if F == 0:
            break
    if F == 1:
        print(A)
        break
