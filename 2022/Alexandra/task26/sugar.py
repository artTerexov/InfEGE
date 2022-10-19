with open('files/sugar.txt') as f:
    s = [(int(i.split()[1]) / int(i.split()[0]), int(i.split()[0]), int(i.split()[1])) for i in f.readlines()]

mass = s[0][2]
s.pop(0)
s.sort()

grandA = [0, 0]
grandB = [0, 0]
ostat = [0, 0]


for i in range(len(s)):
    if grandA[0] + i[1] <= mass:
        grandA[0] += i[1]
        grandA[1] += i[2]
    else:
        grandA[1] += i[0] * (mass - grandA[0])
        ostat = i[1] - grandA[0]
        grandA[0] += (mass - grandA[0])
        continue
print(grandA)
print(grandB)


