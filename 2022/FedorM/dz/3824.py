f = open('27-60b.txt')
n = int(f.readline())
s = [0]
ans = []
for i in range(n):
    x = int(f.readline())
    s += [a + x for a in s] + [x]
    s = {x % 25: x for x in sorted(s)}
    if 0 in s:
        ans.append(s[0])
    s = list(s.values())


ans.sort()
print(max(ans))
