with open("files/test.txt") as f:
    s = f.read().strip().split("\n")

s = [int(i) for i in s]

count = 0
for i in range(len(s) - 11):
    for j in range(i + 11, len(s)):
        if (s[i] + s[j]) < 200:
            count += 1
print(count)