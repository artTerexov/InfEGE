
with open("17.txt") as f:
    s = [int(i) for i in f.read().strip().split("\n")]

s1 = [int(i) for i in s if i % 11 == 0]
a = max(s1)

buff = []
count = 0
for i in range(len(s) - 1):
    if (s[i] % 11 == 0 or s[i + 1] % 11 == 0) and (s[i] + s[i + 1]) <= a:
        buff.append(s[i] + s[i + 1])
        count += 1

print(count, max(buff))

