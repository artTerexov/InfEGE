for i in range(61, 1000):
    x = bin(i)[2:]
    for j in range(3):
        if x.count('0') == x.count('1'):
            x = x + x[-1]
        elif x.count('0') > x.count('1'):
            x = x + '1'
        elif x.count('0') < x.count('1'):
            x = x + '0'
    if int(x, 2) % 4 != 0 and int(x, 2) % 2 == 0:
        print(i)
        break
