for x in range(1001):
    for y in range(1001):
        a = 0
        b = 0
        x1 = x
        y1 = y
        while x1 * y1 > 0:
            if x1 > 0:
                a += 1
            if y1 > 0 and y1 % 7 > b:
                b = y1 % 7
            x1 //= 10
            y1 //= 7
        if a == 4 and b == 5:
            print(x*y)
            break
    if a == 4 and b == 5:
        break
