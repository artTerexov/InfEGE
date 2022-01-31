for i in range(190202, 190261, 2):
    b = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if j % 2 == 0:
                b.add(j)
            if i // j % 2 == 0:
                b.add(i // j)
    if len(b) == 3:
        print(i, max(b))

# 190226 838
# 190234 17294
# 190238 2606
# 190252 95126
# 190258 758