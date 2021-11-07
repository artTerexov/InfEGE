# (Е. Джобс) Исполнитель Вычислитель преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 2
# 2. Сделать простое
# Первая команда увеличивает число на экране на 2, вторая – получает ближайшее бóльшее простое число.
# Сколько существует программ, для которых при исходном числе 2 результатом является число 45 и при этом
# траектория вычислений содержит число 14 и не содержит числа 33?

def simple(num):
    for i in range(num + 1, 46):
        countDel = 2
        for j in range(2, i):
            if i % j == 0:
                countDel += 1
                break
        if countDel == 2:
            return i
    return 46


def calc(start, end, cut, flag):
    if start > end:
        return 0
    if start == cut:
        return 0
    if start == 14:
        flag += 1
    if start == end and flag == 1:
        return 1
    return calc(start + 2, end, cut, flag) + calc(simple(start), end, cut, flag)


print(calc(2, 45, 33, 0))

# for i in range(1, 46):
#     print(i, simple(i))
