# https://inf-ege.sdamgia.ru/problem?id=35913

with open("24-2.txt") as f:
    s = f.read()

m = s.split()
count = 0
b = []
for i in range(0, len(s)):
    if s[i] == "N":
        count += 1
    if s[i] == "\n":
        b.append(count)
        count = 0
c = b.index(min(b))

t = m[c]
k = "QWERTYUIOPASDFGHJKLZXCVBNM"
h = []
maxLetter = ""
maxNum = 0
for j in k:
    if maxNum < t.count(j):
        maxNum = t.count(j)
        maxLetter = j
print(maxLetter)