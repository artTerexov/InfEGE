a = open('files/4752.txt')
d = a.read()
a.close()
c = 0
m = 0
d = d.replace('A', '*')
d = d.replace('E', '*')
d = d.replace('I', '*')
d = d.replace('O', '*')
d = d.replace('U', '*')
d = d.replace('Y', '*')
pr = 0
for i in range(len(d)):
    k = i
    while pr != 8 and (len(d)) != k and d[k] != '.':
        if d[k] == '*':
            pr += 1
        if ((d[k] == '.') or (pr == 8)) == 0:
            c += 1
        k += 1
    m = max(m, c)
    pr = 0
    c = 0
print(m)
