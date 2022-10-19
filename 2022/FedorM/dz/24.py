s = open('24.txt').read()

s = s.replace('AB', '1')
s = s.replace('CAC', '2')
count = 0
maxCount = 0
for i in range(len(s)):
    if s[i] == '1' or s[i] == '2':
        count += 1
    else:
        if count == 14:
            print(s[i - 20: i + 5])
        maxCount = max(count, maxCount)
        count = 0
maxCount = max(count, maxCount)
print(maxCount)