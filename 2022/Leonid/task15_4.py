buff = []
for A in range(1, 10000):
    for x in range(1, 10000):
        F = not(x % 18 == 0) or (not(x % 54 == 0) or (x % A == 0))
        if F == 0:
            break
    if F == 1:
        print(A)

print(min(buff), max(buff))