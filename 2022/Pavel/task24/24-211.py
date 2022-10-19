with open('24-211.txt') as f:
    s = f.read()

a = ["ABEC", "BDAC", "CAFB", "CFBA"]
count = 0
maxCount = 0
i = 0
while i < len(s):
    if s[i:i+4] in a:
        count += 1
        i += 3
    else:
        maxCount = max(maxCount, count)
        count = 0
        i += 1
maxCount = max(maxCount, count)
print(maxCount)
# BDEABECAFBDACBD