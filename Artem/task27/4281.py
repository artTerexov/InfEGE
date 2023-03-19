with open('files/4281_B.txt') as f:
    s = [int(i) for i in f.readlines()]

s.pop(0)
d = 43
a1 = [0] * d
a2 = [0] * d
a2[0] = -1
summ = 0
maxSumma = 0
maxLen = 0

for i in range(len(s)):
    summ += s[i]
    ostat = summ % d
    if a1[ostat] == 0 and ostat != 0:
        a1[ostat] = summ
        a2[ostat] = i
    elif maxSumma < summ - a1[ostat]:
        maxSumma = summ - a1[ostat]
        maxLen = i - a2[ostat]
    elif maxSumma == summ - a1[ostat]:
        maxLen = min(maxLen, i - a2[ostat])


print(maxLen)

