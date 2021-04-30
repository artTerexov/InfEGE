with open('Files/24_2552.txt') as f:
    s = f.read()

count = 0

for i in range(0, len(s)):
    if s[i] == "S" and s[i:i + 7:] == "SOCKCOS":
        count += 1

print(count)
