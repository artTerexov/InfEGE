# Значение выражения 64^11 – 4^10 + 96 – x записали в четверичной системе счисления,
# при этом сумма цифр в записи оказалась равной 71.
# При каком минимальном натуральном x это возможно?

# Функция перевода чисел из 10 в base СС.
def numberTranslation(number, base):
    buff = ""
    while number:
        buff += str(number % base)
        number //= base
    return buff[::-1]


for x in range(0, 20):
    num = 64 ** 11 - 4 ** 10 + 96 - x
    newNum = numberTranslation(num, 4)
    summa = 0
    for i in newNum:
        summa += int(i)
    if summa == 71:
        print(x)
        break