with open("24-157.txt") as f:
    s = f.read().split()

s = s[0].replace("PR", "*")
s = s.replace("RP", "*")

max_count = 0
count = 0
for letter in s:
    if letter == "*":
        count += 1
        if count > max_count:
            max_count = count
        count = 1
    else:
        count += 1

print(max_count)
