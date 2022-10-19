with open('files/26-85.txt') as f:
    s = [[int(j) for j in i.split()]for i in f.read().strip().split('\n')]

s.sort()

count = 0
countN = 0
t = 0
print(s)

for i in range(len(s) - 1):
    if s[i][0] == s[i + 1][0]:
        if s[i][2] == s[i + 1][2] == 1 and s[i + 1][1] - s[i][1] - 1 == 100:
            t += 1