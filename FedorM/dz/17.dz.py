c = 0
d = [int(x) for x in open('17-204.txt')]
mx = -10000
for i in range(2, len(d)):
    if d[i - 2] < 0 and d[i - 2] % 10 != 9 and d[i - 1] > 0 and d[i - 1] % 10 == 9 and d[i] < 0 and d[i] % 10 != 9:
        c += 1
        mx = max(mx, d[i - 2] + d[i - 2] + d[i])
print(c, mx)

