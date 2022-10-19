s = open("test").read()

count = 0
buffer = 0


for i in range(0, len(s)):
    if (s[i] == "X" and count % 3 == 0) or (s[i] == "Y" and count % 3 == 1) or (s[i] == "Z" and count % 3 == 2):
        count += 1
    else:
        buffer = max(buffer, count)
        count = 0
print(buffer)