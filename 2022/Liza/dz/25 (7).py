
for i in range(200000001, 200001000):
    buff = set()
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            if k % 2 != 0:
                buff.add(k)
            if (i // k) % 2 != 0:
                buff.add(i // k)
    if len(buff) >= 6:
        buff = list(buff)
        buff.sort()
        print(i, buff[-6])