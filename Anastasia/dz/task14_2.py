# 3599

num = 4 ** 2016 + 2 ** 2018 - 6
base = 2

buff = ""
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]

print(buff.count("1"))