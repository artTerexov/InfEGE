# Сколько существует чисел, восьмеричная запись которых
# содержит 8 цифр, причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.

import itertools

a = '12345670'
b = itertools.permutations(a, r=8)


result = []
for i in b:
    c = ''.join(i)
    even = '24680'
    odd = '13579'
    flag = 1
    for l in range(1, len(c)):
        if not (((c[l] in even) and (c[l - 1] in odd)) or ((c[l] in odd) and (c[l - 1] in even))):
            flag = 0
            break
    if flag and c[0] != '0':
        result.append(c)

print(len(result))