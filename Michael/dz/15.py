def DEL(x, y):
    if x % y == 0:
        return True
    else:
        return False


k = 0
for A in range(-1000, 10000):
    if A == 0:
        continue
    flag = True
    for x in range(-1000, 10000):
        F = DEL(A, 25) and ((DEL(x, 24) and DEL(x, 75)) <= DEL(x, A))
        if F == 0:
            flag = False
            break
    if flag:
        k += 1
print(k)
