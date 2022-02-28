with open('files/27-13a.txt') as f:
    s = f.read().split()

s.pop(0)
s = [int(i) for i in s]

count = 0
for i in range(len(s) - 7):
    for j in range(i + 7, len(s)):
        if (s[i] * s[j]) % 14 == 0:
            count += 1
            print(s[i], s[j])

print(count)