with open("24-5.txt") as f:
    s = f.read()
count = 0

for i in range(0, len(s)):
    if s[i] == "(" and s[i + 1] == ")":
        count += 1

print(count)