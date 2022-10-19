d = [int(x) for x in open('files/2673.txt')]
c = 0
d.pop(0)
mn = 10 ** 10
for i in range(len(d) - 1):
    for j in range(i + 1, len(d)):
        if (d[i] + d[j]) % 2 != 0:
            continue
        sred = (d[i] + d[j]) // 2
        K = min([abs(sred - n) for n in d])
        if K == 5:
            c += 1
            mn = min(mn, sred)
print(c, mn)