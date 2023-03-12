# НАЧАЛО
# ПОКА нашлось(01) ИЛИ нашлось(02) ИЛИ нашлось(03)
#   заменить(01, 2302)
#   заменить(02, 10)
#   заменить(03, 201)
# КОНЕЦ ПОКА
# КОНЕЦ


for i in range(1, 60):
    for j in range(1, 60):
        for k in range(1, 60):
            s = '0' + '1' * i + '2' * j + '3' * k
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 51 and s.count('2') == 29 and s.count('3') == 23:
                print(k)

