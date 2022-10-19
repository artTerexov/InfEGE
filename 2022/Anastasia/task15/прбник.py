for A in range(-10, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((2 * y + 3 * x != 135) or (y > A) or (x > A)) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
