# НАЧАЛО
#   ПОКА нашлось (53)
#     заменить (53, 8)
#   КОНЕЦ ПОКА
# КОНЕЦ
# Исходная строка содержит 11 троек и некоторое количество пятерок, других цифр нет, точный порядок
# расположения троек и пятерок неизвестен. После выполнения программы
# получилась строка с суммой цифр 118. Какое наименьшее количество пятерок могло быть в исходной строке?

for v in range(30):
    s = '3' * 11 + '5' * v
    k = 0
    while s.find('53') != -1:
        s = s.replace('53', '8', 1)
    for elem in s:
        if elem.isdigit():
            k += int(elem)
    if k == 118:
        print(v)
        break
        