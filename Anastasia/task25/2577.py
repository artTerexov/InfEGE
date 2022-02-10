for a in range(1820348, 2880927 + 1):
    d = set()
    if int(a ** 0.5) ** 2 != a:
        continue
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            d.add(i)
            d.add(a // i)
    if len(d) == 5:
        d = list(d)
        d.sort()
        print(d[-2], d[-1])