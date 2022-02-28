
with open('files/3781.txt') as f:
    s = f.read().strip().split('\n')

minA = 99999999
minIndex = 0

for i in range(len(s)):
    if s[i].count('A') < minA:
        minIndex = i
        minA = s[i].count('A')

letters = set()
for j in s[minIndex]:
    letters.add(j)

maxLetter = ''
maxCount = 0
for l in letters:
    if (maxCount < s[minIndex].count(l)) or (maxCount == s[minIndex].count(l) and maxLetter < l):
        maxCount = s[minIndex].count(l)
        maxLetter = l

print(maxLetter, ''.join(s).count(maxLetter))

