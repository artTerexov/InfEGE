# Сколько существует чисел, шестнадцатеричная запись которых содержит 3 цифры, причём
# все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.

import itertools

s = '0123456789ABCDEF'
a = set(itertools.permutations(s, r=3))
count = 0

for i in a:
    b = ''.join(i)
    flag = True
    for j in range(len(b) - 1):
        if (int(b[j], 16) % 2 != 0 and int(b[j + 1], 16) % 2 != 0) or (int(b[j], 16) % 2 == 0 and int(b[j + 1], 16) % 2 == 0):
            flag = False
            break
    if flag and b[0] != '0':
        count += 1
print(count)

