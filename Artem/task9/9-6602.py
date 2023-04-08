with open('files/9-6602_test') as f:
    a = f.read().split('\n')
a = [list(map(int, a[i].split('\t'))) for i in range(len(a))]
count = 0
for i in range(len(a)):
    l = 0
    pov = 0
    nepov = 0
    for z in a[i]:
        for k in a[i]:
            if z == k:
                l += 1
    if l == 8:
        for z in a[i]:
            p = 0
            for k in a[i]:
                if z == k:
                    p += 1
            if p == 2:
                pov += z
            else:
                nepov += z
        if (nepov / 4) >= pov:
            count += 1
print(count)
