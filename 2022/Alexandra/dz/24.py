with open('24 (3).txt') as f:
    s = f.read()
s = s.replace('BB', '1')
s = s.replace('DD', '2')
count = 0
mx = 0
for i in range(len(s)):
    if s[i] == '1' or s[i] == '2':
        count += 1
    else:
        if count == 316:
            print(s[i - 320: i + 10])
        mx = max(count, mx)
        count = 0
print(mx)
