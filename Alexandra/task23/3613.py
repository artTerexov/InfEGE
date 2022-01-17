# Исполнитель Простачок преобразует число, записанное на экране. У исполнителя есть три команды,
# которым присвоены номера:
# 1. Прибавить 2
# 2. Прибавить 3
# 3. Умножить на 2
# Первая команда увеличивает число на 2, вторая – на 3, третья – увеличивает число вдвое.
# Сколько различных чисел может быть получено из числа 10 всеми возможными алгоритмами длиной 5 команд?


def calc(start, c):
    if c == 5:
        s.add(start)
        return 1
    c += 1
    return calc(start + 2, c) + calc(start + 3, c) + calc(start * 2, c)


s = set()
calc(10, 0)
print(len(s))
