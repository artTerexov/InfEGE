with open('files/27-17b.txt') as f:
    s = [int(i) for i in f.read().strip().split('\n')]

r = s[0]
s.pop(0)

buff = []
buff_2 = []
for i in range(len(s)):
    buff.append((s[i] % 13, s[i] % 2))
    buff_2.append(s[i] % 2)

count = 0
for j in range(len(s) - 5):
    if buff[j][0] != 0:
        if buff[j][1] == 1:
            count += buff[j + 5:].count((0, 0))
        if buff[j][1] == 0:
            count += buff[j + 5:].count((0, 1))
    if buff[j][0] == 0:
        if buff[j][1] == 1:
            count += buff_2[j + 5:].count(0)
        if buff[j][1] == 0:
            count += buff_2[j + 5:].count(1)
print(count)