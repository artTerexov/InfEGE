# Исполнитель Июнь17 преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Сделай нечётное
# Выполняя первую команду, исполнитель увеличивает число на 1, а выполняя вторую – из числа x получает число 2x+1.
# Сколько существует программ, для которых при исходном числе 1 результатом является число 31 и при этом траектория
# вычислений не содержит число 25?
def calc(start, end, cut):
    if start > end:
        return 0
    if start == cut:
        return 0
    if start == end:
        return 1
    return calc(start + 1, end, cut) + calc(2 * start + 1, end, cut)


print(calc(1, 31, 25))