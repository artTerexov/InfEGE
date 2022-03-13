
with open('24-169 (1).txt') as f:
    s = f.read()

s = s.replace('XYZ', '1')


count = 0
maxcount = 0
for i in range(len(s)):
    if s[i] == '1':
        count += 3
    else:
        if count > maxcount:
            maxcount = count + 2
            print(maxcount, i)
        count = 0
print(maxcount)