# 4067

num = 6 ** 333 - 5 * 6 ** 215 + 3 * 6 ** 144 - 85
base = 6

buff = ""
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]

print(buff.count("5"))