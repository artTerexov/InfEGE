with open('files/27-75a.txt') as f:
    s = [int(i) for i in f.read().split()]
s.pop(0)

K = 43
summa = [10 ** 10] * K
d = [0] * K
m = 0
maxSumm = 0
minLen = 0

for i in range(len(s)):
    m += s[i]
    ostat = m % K
    if summa[ostat] == 10 ** 10:
        summa[ostat] = m
        d[ostat] = i
    if m - summa[ostat] > maxSumm:
        maxSumm = m - summa[ostat]
        minLen = i - d[ostat]
    if m - summa[ostat] == maxSumm:
        minLen = min(minLen, i - d[ostat])
print(minLen)
