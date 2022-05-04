import string


with open('files/3781.txt') as f:
    s = f.read().strip().split('\n')

# DFDSFDSFDF\nFDSFDSFSDF\n

countA = 10 ** 10
indexA = 0
for i in range(len(s)):
    if s[i].count('A') < countA:
        countA = s[i].count('A')
        indexA = i

result = []
for j in string.ascii_uppercase:
    result.append((s[indexA].count(j), j))

result.sort()
print(result)
print(''.join(s).count('V'))

print(indexA)