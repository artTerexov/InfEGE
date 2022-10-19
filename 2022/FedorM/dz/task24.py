# d = open('24 (5).txt').read()
d = "BBBDDBBDD"
d = d.replace('BB', '*').replace('DD', '*')
print(d)
c = 0
mx = 0
for i in range(len(d)):
    if d[i] == '*':
        c += 1
    else:
        mx = max(c, mx)
        c = 0
print(mx)

#