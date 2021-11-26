# Автомат обрабатывает натуральное число N < 256 по следующему алгоритму:
# 1) Строится восьмибитная двоичная запись числа N.
# 2) Инвертируются все разряды исходного числа, кроме последней единицы и стоящих за ней нулей (0 заменяется на 1, 1 на 0).
# 3) Полученное число переводится в десятичную систему счисления.
# Для какого значения N результат работы алгоритма равен 11?

for n in range(1, 256):
    b = bin(n)[2:]
    b = "0" * (8 - len(b)) + b
    lastOne = b.rindex("1")
    reversed = ''
    for i in range(len(b)):
        if i < lastOne:
            if b[i] == '1':
                reversed += '0'
            elif b[i] == '0':
                reversed += '1'
        else:
            reversed += b[i]
    r = int(reversed, 2)
    if r == 11:
        print(n)
        break
