# s = open('files/24 (10).txt').read()
# k = ['BB', "DD"]
#
s = 'BBDDBBDDD'
s = s[::-1]
s = s.replace('BB', '1')
s = s.replace('DD', '2')
s = s[::-1]
count = 0
maxCount = 0
i = 0
# print(s)
# s = 'BDEABECAFBDAC'
while i < len(s):
    if s[i] == '1' or s[i] == '2':
        count += 1
        maxCount = max(maxCount, count)
        i += 1
    else:
        if count == 4:
            print(s[i - 3: i + 2])
        maxCount = max(maxCount, count)
        count = 0
        i += 1
print(maxCount)