# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр,
# причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.

import itertools

# 0..7 -> 10305

s = "01234567"
a = set(itertools.permutations(s, r=5))
count = 0

for i in a:
    n = "".join(i)
    flag = True
    for j in range(len(n) - 1):
        if (int(n[j]) % 2 == 0 and int(n[j + 1]) % 2 == 0) or (int(n[j]) % 2 != 0 and int(n[j + 1]) % 2 != 0):
            flag = False
            break
    if flag and n[0] != "0":
        count += 1

print(count)