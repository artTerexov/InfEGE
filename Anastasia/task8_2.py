# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр, причём все цифры
# различны и никакие две чётные и две нечётные цифры не стоят рядом.

import itertools

a = set(itertools.permutations("01234567", r=5))
count = 0
for i in a:
    b = "".join(i)
    if b[0] != "0" and (int(b[0]) % 2 != int(b[1]) % 2) and (int(b[1]) % 2 != int(b[2]) % 2) and (int(b[2]) % 2 != int(b[3]) % 2) and (int(b[3]) % 2 != int(b[4]) % 2):
        count += 1
print(count)