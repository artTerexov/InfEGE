for i in range(50034679, 92136895 + 1):
    a = set()
    if int(i ** 0.5) ** 2 != i:
        continue
    for n in range(2, int(i ** 0.5) + 1):
        if i % n == 0:
            a.add(n)
            a.add(i // n)
    if len(a) == 3:
        print(i, max(a))

