buff = []
v = 1

for i in range(1985, 8529):
    n = str(i)
    if i % 2 != 0 and i % 7 != 0 and i % 47 != 0 and (int(n[-1]) + int(n[-2])) == 6:
        buff.append(i)
        v *= i

print(max(buff), str(v))


# 8515 125