# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр,
# причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.

import itertools

s = "01234567"

a = set(itertools.permutations(s, r=5))

count = 0
for i in a:
    flag = True
    for j in range(len(i) - 1):
        if int(i[j]) % 2 == 0 and int(i[j + 1]) % 2 == 0:
            flag = False
            break
        if int(i[j]) % 2 != 0 and int(i[j + 1]) % 2 != 0:
            flag = False
            break
    if flag and i[0] != "0":
        count += 1
        print(i)
print(count)