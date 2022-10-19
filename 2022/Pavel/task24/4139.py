with open('4139.txt') as f:
    s = f.read()
s = s.replace('XYZ', '1')

count = 0
maxCount = 0
for i in s:
    if i == '1':
        count += 1
    else:
        maxCount = max(maxCount, count)
        count = 0
print(maxCount * 3)