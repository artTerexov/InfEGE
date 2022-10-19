# Сколько существует чисел, шестнадцатеричная запись которых содержит 4 цифры,
# причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.

import itertools

a = set(itertools.permutations("0123456789ABCDEF", r=4))
count = 0

for i in a:
    b = "".join(i)
    if b[0] != "0" and ((int(b[0], 16) % 2) != (int(b[1], 16) % 2) and (int(b[1], 16) % 2) != (int(b[2], 16) % 2) and (int(b[2], 16) % 2) != (int(b[3], 16) % 2)):
        count += 1
print(count)

