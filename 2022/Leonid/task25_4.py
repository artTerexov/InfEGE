buff = []
count = 0

for i in range(250200, 100000000):
    if len(buff) > 0:
        summa = max(buff) + min(buff)
        if summa % 123 == 17:
            count += 1
            print(i - 1, summa)
        if count == 5:
            break
    buff.clear()
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            buff.append(j)