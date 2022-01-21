# Значение выражения (88 + 2·8^x)·8^x + 88 + 8^8, где x > 3 – натуральное число,
# записали в системе счисления с основанием 8. Укажите сумму цифр этой записи.


base = 8
add = []
numadd = 0
for x in range(4, 7):
    num = (88 + 2 * 8 ** x) * 8 ** x + 88 + 8 ** 8
    buff = ''
    while num != 0:
        buff += str(num % base)
        num //= base
    print(buff)
    for i in range(len(buff)):
        numadd += int(buff[i])
    add.append(numadd)
    numadd = 0
print(add)

