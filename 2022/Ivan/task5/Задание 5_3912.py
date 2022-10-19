for n in range(101, 10000):
    b = bin(n)[2:]
    for j in range(3):
        q = b.count("1")
        e = b.count("0")
        if q == e:
            b = b + b[-1]
        elif q > e:
            b = b + "0"
        else:
            b = b + "1"
    r = int(b, 2)
    if r % 4 == 0 and r % 8 != 0:
        print(n)
        break