# Исполнитель Калькулятор преобразует число на экране.
# У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 3
# 3. Умножить на 4
# Программа для исполнителя Калькулятор – это последовательность
# команд. Сколько существует программ, для которых при исходном числе
# 2 результатом является число 60, и при этом траектория вычислений содержит
# число task16 и не содержит число 21?

def calc(n, flag):
    if n == 60 and flag == 1:
        return 1
    if n > 60 or (n == 60 and flag == 0):
        return 0
    if n == 21:
        return 0
    if n == 16:
        flag += 1
    return calc(n + 1, flag) + calc(n * 4, flag) + calc(n * 3, flag)


print(calc(2, 0))