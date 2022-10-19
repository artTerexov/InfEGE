for i in range(4671032, 4671107):
    c = 0
    d = set()

    for n in range(1, int(i ** 0.5) + 1):
        if i % n == 0:
            d.add(n)
            d.add(i // n)

    if len(d) == 2:
        print(d)
