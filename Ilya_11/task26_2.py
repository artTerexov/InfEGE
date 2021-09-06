from bisect import bisect_left

def search(a, x):
    i = bisect_left(a, x)
    # print(i)
    return(i != len(a) and a[i] == x)

with open("26 (1).txt") as f:
    s = f.read().strip().split("\n")
s.pop(0)
s = [int(i) for i in s]
s.sort()
b = []

for i in range(0, len(s) - 1):
    if s[i] % 2 != 0:
        continue
    for j in range(i + 1, len(s)):
        if s[j] % 2 != 0:
            continue
        srednee = (s[i] + s[j]) // 2
        if search(s, srednee):
            b.append(srednee)

print(len(b), min(b))