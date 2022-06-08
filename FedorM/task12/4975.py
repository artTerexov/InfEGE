# НАЧАЛО
# ПОКА НЕ нашлось(00)
#   заменить(01, 210)
#   заменить(02, 3101)
#   заменить(03, 2012)
# КОНЕЦ ПОКА
# КОНЕЦ

for i in range(1, 50):
    for j in range(1, 50):
        for k in range(1, 50):
            s = '0' + '2' * i + '1' * j + '3' * k + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 56 and s.count('2') == 44 and s.count('3') == 19:
                print(i + j + k + 2)