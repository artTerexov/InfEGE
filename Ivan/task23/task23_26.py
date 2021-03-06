# (№ 26) Исполнитель Калькулятор преобразует число на экране.
# У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# Программа для исполнителя Калькулятор – это последовательность команд.
# Сколько существует программ, для которых при исходном числе 2 результатом
# является число 29 и при этом траектория вычислений содержит число 14 и не содержит числа 25?


def calculate(start, flag):
    if start == 29 and flag == 1:
        return 1
    if start > 29:
        return 0
    if start == 25:
        return 0
    if start == 14:
        flag += 1
    return calculate(start + 1, flag) + calculate(start * 2, flag)


print(calculate(2, 0))