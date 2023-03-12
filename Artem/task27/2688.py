with open('files/2685_b.txt') as f:
    s = [[int(i.split()[0]), int(i.split()[1])] for i in f.readlines()]

maxTotal = 0
D = 8
remains = [10 ** 10] * D

for i in s:
    maxTotal += max(i)
    diff = max(i) - min(i)
    r = diff % 8
    if r != 0:
        remainsCopy = remains.copy()
        for k in range(1, D):
            r0 = (r + k) % D
            remainsCopy[r0] = min(remains[r0], remains[k] + diff)
        remainsCopy[r] = min(remains[r], diff)
        remains = remainsCopy

if maxTotal % D != 3:
    e = maxTotal % D
    print(e)

print('A = ', 13130 - 95)
print('B = ', 40382437 - 18)

# 13035 40382419
