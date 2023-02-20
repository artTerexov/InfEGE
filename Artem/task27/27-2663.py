with open('files/27-3b.txt') as f:
    a = f.read().strip()
a = a.split('\n')
a.pop(0)
a = [list(map(int, a[i].split(' '))) for i in range(len(a))]
for i in a:
    i.sort()
minans = 0
raz = []
for i in range(len(a)):
    minans += min(a[i])
    raz.append(a[i][1] - a[i][0])
raz.sort()
print(minans)
for i in range(len(raz) - 2):
    if (minans + raz[i]) % 3 == 0:
        minans += raz[i]
        break
    elif (minans + raz[i + 1]) % 3 == 0:
        minans += raz[i + 1]
        break
    elif (minans + raz[i] + raz[i + 1]) % 3 == 0 and (
            ((minans + raz[i + 2]) % 3 == 0 and (minans + raz[i] + raz[i + 1]) < (minans + raz[i + 2])) or (
            minans + raz[i + 2]) % 3 != 0):
        minans += raz[i + 1] + raz[i]
        break
    elif (minans + raz[i + 2]) % 3 == 0:
        minans += raz[i + 2]
        break
print(minans)
