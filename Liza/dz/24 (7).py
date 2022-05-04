with open('24 (3).txt') as f:
    s = f.read()

pr = s.split('PR')
st = s.split('ST')
c = ''
maxcount = 0
for i in range(len(pr)):
    if len(pr[i]) > maxcount:
        maxcount = len(pr[i])
        c = pr[i]

for i in range(len(st)):
    if len(st[i]) > maxcount:
        maxcount = len(st[i])
        c = st[i]

print(maxcount)
print(len(c))