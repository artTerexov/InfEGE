buff = []
for R in range(1, 10000):
    flag = 1
    for A in range(1, 1000):
        for x in range(1, 1000):
            if ((not((x & 108 == 0) or (x & 60 == 0)) or (x & A == 0)) or (x & R == 0)) == 0:
                flag = 0
                break
        if not flag:
            break
    if flag:
        buff.append(R)

print(len(buff))