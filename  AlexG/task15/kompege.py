for A in range(0, 100):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x + y <= 32) or (y <= x + 4) or (y >= A)) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
