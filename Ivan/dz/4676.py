with open("4676.txt") as f:
    s = f.read().strip().split("\n")

s = [int(i) for i in s]
buff = []
sr = sum(s) / len(s)
for i in range(len(s) - 2):
    if s[i] < sr or s[i + 1] < sr or s[i + 2] < sr:
        c = 0
        if abs(s[i]) % 10 == 4:
            c += 1
        if abs(s[i + 1]) % 10 == 4:
            c += 1
        if abs(s[i + 2]) % 10 == 4:
            c += 1
        if c >= 2:
            buff.append(s[i] + s[i + 1] + s[i + 2])
print(len(buff), max(buff))
