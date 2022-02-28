for i in range(358633892, 535672891 + 1):
    d = set()
    if int(i ** 0.5) ** 2 != i:
        continue
    for n in range(2, int(i ** 0.5) + 1):
        if i % n == 0:
            d.add(n)
            d.add(i // n)
        if len(d) > 3:
            break
    if len(d) == 3:
        print(i, max(d))

