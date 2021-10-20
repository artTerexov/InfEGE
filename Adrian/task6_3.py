# Получив на вход некоторое натуральное число X, этот алгоритм печатает
# одно число. Укажите второе (по возрастанию) число Х, для которого алгоритм хоть
# что-нибудь напечатает. Для решения задачи нужно написать программу, выполняющую перебор.

for i in range(1, 100):
    x = i
    b = 0
    while x < 100 and b < 200:
        if x % 2 < 1:
            x = x // 2
        else:
            x = 3 * x + 1
        b += 1
    if b != 200:
        print(i)
