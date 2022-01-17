# 4^230 + 8^120 – 2^150 – 100?

num = 4 ** 230 + 8 ** 120 - 2 ** 150 - 100
base = 2
result = ""

while num != 0:
    result += str(num % base)
    num = num // base
result = result[::-1]

print(result)

print(result.count('0'))
