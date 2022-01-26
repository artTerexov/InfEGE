# Дана программа для исполнителя Редактор:
# НАЧАЛО
# ПОКА нашлось(01) ИЛИ нашлось(02) ИЛИ нашлось(03)
#   заменить(01, 30)
#   заменить(02, 3103)
#   заменить(03, 1201)
# КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка, содержащая 31 единицу, 24 двойки и 46 троек.
# Сколько троек было в исходной строке?


for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            s = '0' + '1' * i + '2' * j + '3' * k

            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1201', 1)

            if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
                print(k)
