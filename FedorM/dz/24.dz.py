d = open('24-157-1.txt')
f = d.readline()
f = f.replace('QW', '*')
c = 0
mx = 0
nflag = 0
for i in range(len(f)):
    if f[i] != '*':
        c += 1
    if f[i] == '*':
        if (nflag == 0) or i == len(f):
            mx = max(mx, c + 2)

        else:
            mx = max(mx, c + 2)
        c = 0
print(mx)
