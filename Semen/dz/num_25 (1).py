s = [""] + [str(i) for i in range(100)]
buff = []
for i in s:
    x = int("12" + i + "6789")
    if x % 39 == 0 and x <= 10 ** 8:
        buff.append([x, x // 39])
buff.sort()
for i in range(len(buff)):
    print(*buff[i])