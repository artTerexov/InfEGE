with open("files/5379") as f:
    s = [int(i) for i in f.readlines()]

count = 0
s.sort(reverse=True)
for i in range(len(s)):
    if i < 2500:
        count += s[i] // 2
    else:
        count += s[i]

rilcount = 0
s.sort()
for i in range(len(s)):
    if i < 2500:
        rilcount += s[i] // 2
    else:
        rilcount += s[i]

print(count, rilcount)


