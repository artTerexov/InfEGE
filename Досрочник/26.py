with open('26 (6).txt') as f:
    s = f.read().strip().split('\n')

s.pop(0)
s = [(int(i.split()[0]), int(i.split()[1])) for i in s]
s.sort(reverse=True)
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i][0] == s[j][0]:
            if s[i][1] - s[j][1] == 12:
                print(s[i][0], s[j][1] + 1)
        else:
            break

# n^2
