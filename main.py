for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            if not((75 != 2 * x + 3 * y) or (A > 3*x) or (A > 2*y)):
                flag = False
                break
    if flag:
        print(A)