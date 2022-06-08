with open("111.txt") as f:
    s = f.read().strip().split("\n")
s = [int(i) for i in s]
buff = []
count = 0
sr = sum(s) / len(s)
for i in range(1, len(s) - 2):
    if (s[i] * s[i + 1]) > (s[i - 1] * s[i + 2]) and (s[i] > sr or s[i + 1] > sr):
        buff.append(s[i] + s[i + 1])

print(len(buff), max(buff))