# Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть две команды,
# которым присвоены номера:
# 1. Прибавь 1
# 2. Прибавь 2
# Первая команда увеличивает число на 1, вторая – на 2. Сколько существует таких программ,
# которые исходное число 3 преобразуют в число 13, и при этом траектория вычислений не содержит 8?

def calc(start):
    if start == 13:
        return 1
    if start > 13 or start == 8:
        return 0
    return calc(start + 1) + calc(start + 2)


print(calc(3, 0))