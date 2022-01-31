for i in range(190202, 190261):
    b = set()
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if j % 2 == 0:
                b.add(j)
            if (i // j) % 2 == 0:
                b.add(i//j)
            if len(b) > 4:
                break
    if len(b) == 4:
        b = list(b)
        b.sort()
        print(b[-1], b[-2])
