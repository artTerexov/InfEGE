import time
start = time.time()

for a in range(3, 300000):
    buff = set()
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            buff.add(b)
            buff.add(a // b)
        if len(buff) > 2:
            break
    if len(buff) == 2:
        # print(buff)
        continue

print(time.time() - start)


# 174457

