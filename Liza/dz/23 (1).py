# Исполнитель Нолик преобразует двоичное число, записанное на экране.
# У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Добавить слева 1
# Первая команда увеличивает число на 1. Вторая команда приписывает к двоичному числу слева 1,
# например, для числа 10 результатом работы данной команды будет являться число 110.
# Сколько существует программ, которые исходное двоичное число 1 преобразуют в двоичное число 11111?


def calc(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return calc(start + 1, end) + calc(int('1' + (bin(start)[2:]), 2), end)


print(calc(1, 31))
