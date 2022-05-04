d = [int(x) for x in open('test.txt')]
d.pop(0)
mn = 100000000000
pos = 0
middle = len(d) // 2
for j in range(len(d)):
    s = 0
    for i in range(1, middle + 1):
        if i == middle:
            s += d[j - i] * i
        else:
            s += d[(j + i) % (len(d))] * i + d[j - i] * i
    if mn > s:
        mn = s
        pos = j + 1
print(pos)

a = []
a.