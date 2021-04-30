# Исполнитель Калькулятор преобразует число, записанное на экране.
# У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавь 1
# 2. Прибавь 2
# 3. Прибавь 3
# Сколько существует программ, которые преобразуют исходное число 5 в число 18, и
# при этом траектория вычислений содержит число 11 и не содержит чисел 10 и 15?

def calc(n, flag) -> str:
    if n == 18 and flag:
        return 1
    if n > 18 or (n == 18 and not flag):
        return 0
    if n == 10 or n == 15:
        return 0
    if n == 11:
        flag = True
    return calc(n + 1, flag) + calc(n + 2, flag) + calc(n + 3, flag)


print(calc(5, False))
