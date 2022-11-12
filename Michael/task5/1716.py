c = 0

for N in range(900, 1000):
    el = []
    for k in str(N):
        el.append(k)
    el.sort()
    x = int(el[2] + el[1])
    if el[0] == "0" and el[1] == "0":
        y = x
    elif el[0] == 0:
        y = int(el[1] + el[0])
    else:
        y = int(el[0] + el[1])
    print(N, x, y)
    if x - y == 70:
        c += 1
print(c)