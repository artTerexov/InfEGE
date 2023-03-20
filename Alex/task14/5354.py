# 343^1515 – 6∙49^1520 + 5∙49^1510 – 3∙7^1530 – 1550

num = 343 ** 1515 - 6 * 49 ** 1520 + 5 * 49 ** 1510 - 3 * 7 ** 1530 - 1550
base = 7
result = ""

while num != 0:
    result = str(num % base) + result
    num = num // base

print(result.count('0'))
