with open('26-39.txt') as f:
    a = f.read().strip().split('\n')

gp = int(a[0].split()[1])
a.pop(0)
imp = [] #180-200
not_imp = []
for i in a:
    if 180 <= int(i) <= 200:
        imp.append(int(i))
    else:
        not_imp.append(int(i))
gp -= sum(imp)
s = gp
not_imp.sort()
# print(not_imp)
for i in range(len(not_imp)):
    if gp >= not_imp[i]:
        gp -= not_imp[i]
    else:
        print(gp, i)
        break
amount = len(imp) + 102
gp += not_imp[101]
e = 102
while gp > not_imp[e]:
    e += 1
else:
    if gp == not_imp[e]:
        gp -= not_imp[e]
    else:
        gp -= not_imp[e - 1]
print(gp)
print(f'Ответ: {amount}, 10000')
