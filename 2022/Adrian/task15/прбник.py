for A in range(-10, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((2 * y + 3 * x != 135) or (y > A) or (x > A)) == 0:
                flag = False
                break
    if flag == True:
        print(A)
