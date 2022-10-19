buff = []
for i in range(1, 1000):
    d = i
    n = 8
    s = 78
    while s <= 1200:
        s = s + d
        n = n + 2
    if n == 46:
        buff.append(i)

print(buff)
