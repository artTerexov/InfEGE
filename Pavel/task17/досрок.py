with open('files/досрок.txt') as f:
    s = [int(i) for i in f.readlines()]

min17 = 1000000
buff = []
for i in s:
    if i % 17 == 0:
        min17 = min(min17, i)

for i in range(len(s) - 1):
    if s[i] % min17 == 0 or s[i + 1] % min17 == 0:
        buff.append(s[i] + s[i + 1])

print(len(buff), max(buff))