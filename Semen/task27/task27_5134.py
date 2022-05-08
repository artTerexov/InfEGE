import time

start = time.time()

with open('files/5134_B.txt') as f:
    s = [int(i) for i in f.read().split()][1:]
result = 0
M = 524288
for i in range(len(s)):
    product = s[i]
    if product % M != 0:
        result += 1
    else:
        continue
    for j in range(i + 1, len(s)):
        product *= s[j]
        if product % M != 0:
            result += 1
        if s[j] % M == 0:
            break
print(result)

print(time.time() - start)

