# Сколько единиц содержится в двоичной записи значения выражения: 8^2020 + 4^2017 + 26 – 1?

num = 8 ** 2020 + 4 ** 2017 + 26 - 1
base = 2

buff = ""
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]

print(buff.count("1"))


