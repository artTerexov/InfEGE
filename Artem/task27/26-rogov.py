with open('files/26-rogov.txt') as f:
    a = f.read().strip()
a = a.split('\n')
k = int(a.pop(0))
a.pop(0)
a = [[int(a[i].split()[0]), int(a[i].split()[1])] for i in range(len(a))]
d = [0] * k
c = 0
vr = 0
a.sort()
for i in range(len(a)):
    flag = True
    for z in range(len(d)):
        if d[z] < a[i][0]:
            d[z] = a[i][1] + a[i][0]
            for g in range(len(d)):
                if d[g] < a[i][0]:
                    d[g] = 0
            if d.count(0) == 0:
                vr += abs(a[i][0] - min(d)) - 1
            flag = False
            break
    if flag:
        c += 1
print(c, vr)


# 523 534