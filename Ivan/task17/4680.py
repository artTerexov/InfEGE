with open("files/4680.txt") as f:
    s = f.read().strip().split("\n")

s = [int(i) for i in s]
buff = []

arf = sum(s) / len(s)

for i in range(len(s) - 2):
    if (s[i] > arf and s[i + 1] > arf) or (s[i + 1] > arf and s[i + 2] > arf) or (s[i] > arf and s[i + 2] > arf):
        buff.append(s[i] + s[i + 1] + s[i + 2])

print(len(buff), max(buff))

