#  Исполнитель Нолик преобразует двоичное число, записанное на экране. У исполнителя есть две команды, которым присвоены
#  номера:
# 1. Вычесть 1
# 2. Обнулить
# Первая команда уменьшает число на 1. Вторая команда обнуляет все ненулевые разряды, кроме старшего (например,
# для исходного числа 11101 результатом работы команды будет число 10000), если таких разрядов нет, то данная команда
#  не выполняется.
# Сколько существует программ, которые исходное двоичное число 10001 преобразуют в двоичное число 1?

def Zamena(a):
    c = '1'
    a = bin(a)[2:]
    count = 0
    for i in range(1, len(a)):
        if a[i] == '1':
            c += '0'
            count += 1
        else:
            c += '0'
    if count == 0:
        return 0
    else:
        return int(c, 2)
#
#
# def Vychet(a):
#     return bin(int(a, 2) - 1)[2:]
#
#
# def F(a, b):
#     if a == b:
#         return 1
#     if int(a, 2) < int(b, 2):
#         return 0
#     return F(Vychet(a), b) + F(Zamena(a), b)
#
#
# print(F('10001', '1'))


def F(a, b):
    if a == b:
        return 1
    if a < 1:
        return 0
    print(a)
    return F(a - 1, b) + F(Zamena(a), b)


print(int('10001', 2))
print(F(int('10001', 2), 1))

