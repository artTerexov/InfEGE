with open('files/27-74b.txt') as f:
    a = f.read()
a = [int(i) for i in a.strip().split('\n')]
a.pop(0)
sum = 0
D = 39
k = 20
a1 = [[] for i in range(D)]
a2 = [[] for i in range(D)]
l = 0
for i in range(len(a)):
    sum += a[i]
    ostat = sum % D
    if sum % 39 == 0 and (i + 1) <= k:
        l += 1
    a1[ostat].append(sum)
    a2[ostat].append(i + 1)
    for j, el in enumerate(a2[ostat]):
        if 0 < ((i + 1) - el) <= k:
            # print((i + 1) - el, sum - a1[ostat][j])
            l += 1
print(l)