with open('files/5373.txt') as f:
    s = [int(i) for i in f.readlines()]


minNumber = 10 ** 10
result = list()

for i in s:
    if i > 0 and i % 19 == 0:
        minNumber = min(minNumber, i)

for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) < minNumber:
        result.append(s[i] + s[i + 1])

print(len(result), max(result))

# 4984 696

