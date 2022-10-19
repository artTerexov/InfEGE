with open('files/24.txt') as f:
    s = f.read()

s = s.replace('AB', '*')
s = s.replace('AC', '*')

count = 0
maxCount = 0

print(s)
for i in s:
    if i == '*':
        count += 1
    else:
        maxCount = max(maxCount, count)
        count = 0
print(maxCount)