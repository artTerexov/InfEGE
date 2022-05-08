import string

with open('files/духота.txt') as f:
    s = f.read().strip().split('\n')

maxStr = ''

for i in s:
    a = i.split('A')
    a.sort(key=lambda k: len(k))
    if len(maxStr) < len(a[-1]):
        maxStr = a[-1]

result = []

for i in string.ascii_uppercase:
    result.append((maxStr.count(i), i))

print(max(result))
print('M', ''.join(s).count('M'))

#