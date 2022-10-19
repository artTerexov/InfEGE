
with open("files/26.txt") as f:
    s =[[int(j) for j in i.split()]for i in f.read().strip().split("\n")]

s.pop(0)
s.sort()
count = 0
buff = []
for i in range(len(s) - 1):
    if s[i][0] == s[i + 1][0] and s[i + 1][1] - s[i][1] - 1 == 0:
        count += 1
    else:
        if s[i][0] == s[i + 1][0] and s[i][1] == s[i + 1][1]:
            count += 1
            continue
        if s[i][0] != s[i + 1][0] or s[i + 1][1] - s[i][1] - 1 != 0 or s[i][1] != s[i + 1][1]:
            buff.append([count + 1, s[i][0]])
            count = 0

buff.sort()
print(buff)
for i in buff:
    if i[0] == 7:
        print(i)