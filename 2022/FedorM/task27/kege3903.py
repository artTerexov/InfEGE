s = open('files/27-B (2).txt').read().strip().split('\n')

d = int(s[0].split()[1])
s.pop(0)
s = [int(i) for i in s]
countTrack = 0
c = sum([1 for k in s if k > 0])
for i in range(100000):
    countTrack += 1
    t = 0
    j = 0
    while j < len(s):
        if s[j] > 0:
            if t + s[j] > d:
                s[j] = t + s[j] - d
                t = d
                j += 1
            else:
                t += s[j]
                s.pop(j)
                c -= 1
        elif s[j] < 0:
            if t + s[j] < 0:
                t = 0
                s[j] -= t
                j += 1
            else:
                t += s[j]
                s[j] = 0
                s.pop(j)
        else:
            s.pop(j)
    if c == 0:
        break
print(countTrack)