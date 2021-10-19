# 4065
# Значение выражения 4^103 + 3∙4^444 – 2∙4^44 + 67 записали в системе счисления с основанием 4.
# Сколько цифр 3 содержится в этой записи?
num = 4 ** 103 + 3 * 4 * 444 - 2 * 4 ** 44 + 67
base = 4

buff = ""
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]

print(buff.count("3"))
print(buff)