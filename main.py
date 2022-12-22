# a = 'babababa'
a = 'babbbaba'

c = 0
cmax = 0
for i in range(0, len(a) - 1, 2):
    if a[i] == 'b' and a[i + 1] == 'a':
        c += 1
    else:
        cmax = max(cmax, c)
        c = 0
print(c)