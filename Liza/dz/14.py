# Сколько значащих нулей в двоичной записи числа
#   4^512 + 8^512 – 2^128 – 250


num = 4 ** 512 + 8 ** 512 - 2 ** 128 - 250

a = bin(num)
print(a)
b = str(a).count('0')
print(b)
