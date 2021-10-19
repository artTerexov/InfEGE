# 2206
num = (2 * 343 ** 123 + 2401) * (3 * 343 ** 137 - 2401)
base = 7

buff = ""
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]

print(buff.count("6"))