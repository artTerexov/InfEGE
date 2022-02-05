
for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((((3 * x) + (4 * y)) != 48) or ((A > x) and (A > y))) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break