f = open("24-s1.txt")
s = f.read()
f.close()

count = 0
buffer = 0

for i in range(0, len(s)):
    if s[i] == "A" and s[i + 2] == "R" and s[i + 1] != "\n":
        count += 1
    if s[i] == "\n":
        if count != 0:
            buffer += 1
        count = 0
print(buffer)