# Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть
# три команды, которым присвоены номера:
# 1. Прибавь 1
# 2. Прибавь 2
# 3. Умножь на 3
# Сколько существует программ, которые преобразуют исходное число 1 в число task15, и
# при этом траектория вычислений содержит число 10 и не содержит числа 14?

def F(n, m, flag):
    if n == m and flag == 1:
        return 1
    if n > m:
        return 0
    if n == 14:
        return 0
    if n == 10:
        flag = 1
    return F(n + 1, m, flag) + F(n + 2, m, flag) + F(n * 3, m, flag)


print(F(1, 15, 0))