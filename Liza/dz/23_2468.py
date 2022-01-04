# 1. Прибавить 1
# 2. Прибавить 2
# 3. Умножить на 2
# Программа для исполнителя Калькулятор – это последовательность команд.
# Сколько существует программ, для которых при исходном числе 1 результатом является число 12,
# и при этом траектория вычислений содержит числа 7 и 10?


def calc(start, end, flag):
    if start == end and flag == 2:
        return 1
    if start > end:
        return 0
    if start == 7 or start == 10:
        flag += 1
    return calc(start + 1, end, flag) + calc(start * 2, end, flag) + calc(start + 2, end, flag)


print(calc(1, 12, 0))