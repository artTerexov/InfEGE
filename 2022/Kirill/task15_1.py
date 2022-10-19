# https://inf-ege.sdamgia.ru/problem?id=16045

for A in range(1000, 0, -1):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (y + 2*x != 48) or A < x or A < y
            if F != 1:
                break
        if F != 1:
            break
    if F == 1:
        print("Удовл A = ", A)
        break