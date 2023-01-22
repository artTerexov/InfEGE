with open("files/5263.txt") as f:
    s = f.read()

i = 0
count = 0
maxCount = 0
while i < len(s) - 4:
    if s[i:i + 4] in ['ABEC', 'BDAC', 'CAFB', 'CFBA']:
        count += 1
        i += 3
    else:
        maxCount = max(maxCount, count)
        count = 0
        i += 1
print(maxCount)
