for n in range(1, 1000):
    a = bin(n)[2:]
    for i in range(2):
        b = a.count("1")
        a += str(b % 2)
    r = int(a, 2)
    if r < 114:
        print(r)

