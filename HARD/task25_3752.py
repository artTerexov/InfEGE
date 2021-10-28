import time

start_time = time.time()
dell = []
flag = 0
for i in range(103000000, 104000000, 2):
    if flag == 3:
        dell.sort()
        print(i - 2, dell[2])
    dell.clear()
    flag = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            dell.append(j)
            if j % 2 == 0:
                flag += 1
            if j != i // j:
                dell.append(i // j)
                if (i // j) % 2 == 0:
                    flag += 1
        if flag > 3:
            break
print("--- %s seconds ---" % (time.time() - start_time))
