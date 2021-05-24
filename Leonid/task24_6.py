s = open("24-j5.txt").read()
count = 0
for i in range(0, len(s)):
    if s[i: i + 3] == "OCK" and s[i - 2: i] != "ST":
        count += 1
print(count)