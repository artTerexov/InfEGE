from string import ascii_uppercase

s = open("24.txt").read()

arr = []

maximum = 0

for i in range(0, len(s) - 1):
    if s[i] == "E":
        arr.append(s[i + 1])
for j in ascii_uppercase:
    print(j, arr.count(j))
    maximum = max(maximum, arr.count(j))
print(maximum)
