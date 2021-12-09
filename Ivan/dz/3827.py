buff = []
count = 0
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((A % 35 == 0) and (730 % x == 0) <= ((not(A % x == 0)) <= (not(110 % x == 0)))) == 0:
            flag = False
            break
    if flag:
        count += 1

print(count)