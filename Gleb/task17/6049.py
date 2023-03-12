with open('files/6049_test.txt') as f:
    s = [int(i) for i in f.readlines()]

maxNine = 0
for i in s:
    if str(i)[-1] == '9':
        maxNine = max(maxNine, i)

result = []
for i in range(len(s) - 1):
    num1 = s[i]
    num2 = s[i + 1]
    if ((str(num1)[-1] == '9' and str(num2)[-1] != '9') or (str(num1)[-1] != '9' and str(num2)[-1] == '9')) and (num1 ** 2 + num2 ** 2) < maxNine ** 2:
        result.append(num1 ** 2 + num2 ** 2)

print(len(result), min(result))

# 1428 356530