buff = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((A % 9 == 0) and (280 % x == 0) <= ((not(A % x == 0)) <= (not(730 % x == 0)))) == 0:
            flag = False
            break
    if flag:
        buff.append(A)

print(min(buff))